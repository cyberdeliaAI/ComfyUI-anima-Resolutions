"""Alignment and image-scaling nodes for Anima workflows."""

from functools import lru_cache

def _round_up(value, multiple):
    if multiple <= 1:
        return int(value)
    return int(((int(value) + multiple - 1) // multiple) * multiple)


@lru_cache(maxsize=1)
def _build_hook_class():
    """Import the Impact base class lazily and build our hook subclass."""
    try:
        from impact.hooks import DetailerHook
    except ImportError as exc:
        raise RuntimeError(
            "Anima Detailer Align Hook requires ComfyUI Impact Pack. "
            "Install or update Impact Pack, restart ComfyUI, and try again."
        ) from exc

    class _AnimaAlignHook(DetailerHook):
        def __init__(self, alignment):
            super().__init__()
            self.alignment = int(alignment)

        def touch_scaled_size(self, w, h):
            if self.alignment <= 1:
                return w, h
            return _round_up(w, self.alignment), _round_up(h, self.alignment)

    return _AnimaAlignHook


class AnimaDetailerAlignHook:
    """Creates an Impact-compatible DETAILER_HOOK that aligns crop sizes."""

    DESCRIPTION = (
        "Rounds Impact Pack detailer sampling sizes up to the selected multiple. "
        "Use 32 for Anima workflows."
    )

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "alignment": (["none", "8", "16", "32", "64"], {"default": "32"}),
            },
        }

    RETURN_TYPES = ("DETAILER_HOOK",)
    RETURN_NAMES = ("detailer_hook",)
    FUNCTION = "build"
    CATEGORY = "Anima/Detailer"

    def build(self, alignment):
        multiple = 1 if alignment == "none" else int(alignment)
        hook_cls = _build_hook_class()
        return (hook_cls(multiple),)


_UPSCALE_METHODS = ["nearest-exact", "bilinear", "area", "bicubic", "lanczos"]


class AnimaImageScaleByMultiple:
    """Scale an image by the nearest ratio that keeps W and H on a multiple."""

    DESCRIPTION = (
        "Scales an image and snaps its width and height to a multiple. "
        "Uses ComfyUI's native resize methods, including Lanczos."
    )

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "scale_by": ("FLOAT", {"default": 1.5, "min": 0.1, "max": 8.0, "step": 0.05}),
                "upscale_method": (_UPSCALE_METHODS, {"default": "lanczos"}),
                "multiple": (["8", "16", "32", "64"], {"default": "32"}),
                "max_long_edge": ("INT", {"default": 0, "min": 0, "max": 16384, "step": 8}),
            },
        }

    RETURN_TYPES = ("IMAGE", "INT", "INT", "FLOAT")
    RETURN_NAMES = ("image", "width", "height", "applied_scale")
    FUNCTION = "scale"
    CATEGORY = "Anima/Image"

    def scale(self, image, scale_by, upscale_method, multiple, max_long_edge):
        from comfy.utils import common_upscale

        mult = int(multiple)
        _, src_h, src_w, _ = image.shape

        target_w = src_w * scale_by
        target_h = src_h * scale_by

        if max_long_edge > 0:
            longest = max(target_w, target_h)
            if longest > max_long_edge:
                cap_ratio = max_long_edge / longest
                target_w *= cap_ratio
                target_h *= cap_ratio

        new_w = max(mult, int(round(target_w / mult) * mult))
        new_h = max(mult, int(round(target_h / mult) * mult))

        applied_scale = ((new_w / src_w) + (new_h / src_h)) / 2.0

        samples = image.movedim(-1, 1)
        scaled = common_upscale(
            samples,
            new_w,
            new_h,
            upscale_method,
            "disabled",
        )
        scaled = scaled.movedim(1, -1).clamp(0.0, 1.0)

        return (scaled, new_w, new_h, applied_scale)


NODE_CLASS_MAPPINGS = {
    "AnimaDetailerAlignHook": AnimaDetailerAlignHook,
    "AnimaImageScaleByMultiple": AnimaImageScaleByMultiple,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "AnimaDetailerAlignHook": "Anima Detailer Align Hook",
    "AnimaImageScaleByMultiple": "Anima Image Scale By Multiple",
}

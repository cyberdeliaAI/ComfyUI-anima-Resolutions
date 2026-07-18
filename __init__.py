"""comfyui-anima-resolutions - Cyberdelia."""

from .anima_alignment_nodes import (
    NODE_CLASS_MAPPINGS as _alignment_classes,
    NODE_DISPLAY_NAME_MAPPINGS as _alignment_names,
)
from .anima_resolutions import (
    NODE_CLASS_MAPPINGS as _resolution_classes,
    NODE_DISPLAY_NAME_MAPPINGS as _resolution_names,
)

NODE_CLASS_MAPPINGS = {**_resolution_classes, **_alignment_classes}
NODE_DISPLAY_NAME_MAPPINGS = {**_resolution_names, **_alignment_names}

# Tells ComfyUI to serve everything in ./js as static frontend files
# and auto-load any .js files there as frontend extensions.
WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

class AnimaResolutions:
    """
    A ComfyUI node for selecting Anima-friendly first-pass image resolutions.
    """

    # Resolution mappings with all ratio options.
    RESOLUTIONS = {
        "1024": [
            "1024x1024 (1:1)",
            "1152x896 (9:7)",
            "896x1152 (7:9)",
            "1152x864 (4:3)",
            "864x1152 (3:4)",
            "1344x896 (3:2)",
            "1248x832 (3:2)",
            "896x1344 (2:3)",
            "832x1248 (2:3)",
            "1280x720 (16:9)",
            "720x1280 (9:16)",
            "1344x576 (21:9)",
            "576x1344 (9:21)",
        ],
        "1280": [
            "1280x1280 (1:1)",
            "1440x1120 (9:7)",
            "1120x1440 (7:9)",
            "1472x1104 (4:3)",
            "1104x1472 (3:4)",
            "1536x1024 (3:2)",
            "1024x1536 (2:3)",
            "1536x864 (16:9)",
            "864x1536 (9:16)",
            "1680x720 (21:9)",
            "720x1680 (9:21)",
        ],
        "1536": [
            "1536x1536 (1:1)",
            "1728x1344 (9:7)",
            "1344x1728 (7:9)",
            "1728x1296 (4:3)",
            "1296x1728 (3:4)",
            "1872x1248 (3:2)",
            "1248x1872 (2:3)",
            "2048x1152 (16:9)",
            "1152x2048 (9:16)",
            "2016x864 (21:9)",
            "864x2016 (9:21)",
        ],
    }

    @classmethod
    def INPUT_TYPES(cls):
        resolution_options = list(cls.RESOLUTIONS.keys())

        all_ratios = []
        for ratios in cls.RESOLUTIONS.values():
            all_ratios.extend(ratios)
        all_ratios = list(dict.fromkeys(all_ratios))

        return {
            "required": {
                "resolution": (resolution_options, {"default": "1024"}),
                "ratio": (all_ratios, {"default": "1024x1024 (1:1)"}),
            },
        }

    RETURN_TYPES = ("INT", "INT", "INT")
    RETURN_NAMES = ("resolution", "width", "height")
    FUNCTION = "get_dimensions"
    CATEGORY = "Anima/resolution"

    def get_dimensions(self, resolution, ratio):
        dimensions = ratio.split(" ")[0]
        width, height = dimensions.split("x")

        return (int(resolution), int(width), int(height))


NODE_CLASS_MAPPINGS = {
    "AnimaResolutions": AnimaResolutions,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AnimaResolutions": "Anima Resolutions",
}

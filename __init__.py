"""comfyui-anima-resolutions - Cyberdelia."""

from .anima_resolutions import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# Tells ComfyUI to serve everything in ./js as static frontend files
# and auto-load any .js files there as frontend extensions.
WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

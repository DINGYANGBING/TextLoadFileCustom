"""
TextLoadFileCustom - Enhanced TextLoadFile node for ComfyUI.

Adds the ability to manually specify a folder path or a full file path,
instead of being limited to ComfyUI's default input directory.
"""

from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./js"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]

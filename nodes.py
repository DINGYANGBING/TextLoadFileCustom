"""
Enhanced TextLoadFile node for ComfyUI.

Features:
- Original behavior preserved: lists .txt files from ComfyUI's default input directory.
- NEW: `folder_path` lets you manually specify any folder on disk; the node will
  read the selected (or manually typed) .txt file from that folder.
- NEW: `file_path` lets you directly specify the full path to a .txt file,
  bypassing the dropdown entirely. It takes the highest priority.

Priority when resolving the file:
    1. file_path (full path, highest priority)
    2. folder_path + text_file (manual folder)
    3. ComfyUI default input directory + text_file (original behavior)
"""

import os

import folder_paths


class TextLoadFile:
    """Original RES4LYF node, kept for backward compatibility."""

    @classmethod
    def INPUT_TYPES(cls):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir)
                 if os.path.isfile(os.path.join(input_dir, f)) and f.lower().endswith('.txt')]
        return {
            "required": {
                "text_file": (sorted(files), {"text_upload": True})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "main"
    CATEGORY = "RES4LYF/text"

    def main(self, text_file):
        input_dir = folder_paths.get_input_directory()
        text_file_path = os.path.join(input_dir, text_file)
        if not os.path.exists(text_file_path):
            print(f"Error: The file `{text_file_path}` cannot be found.")
            return ("",)
        with open(text_file_path, "r", encoding="utf-8") as f:
            text = f.read()
        return (text,)


class TextLoadFileAdvanced:
    """TextLoadFile with manual folder / file path support."""

    @classmethod
    def INPUT_TYPES(cls):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir)
                 if os.path.isfile(os.path.join(input_dir, f)) and f.lower().endswith('.txt')]
        return {
            "required": {
                "text_file": (sorted(files), {"text_upload": True}),
            },
            "optional": {
                "folder_path": ("STRING", {"default": "", "forceInput": True, "multiline": False}),
                "file_path": ("STRING", {"default": "", "forceInput": True, "multiline": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "main"
    CATEGORY = "RES4LYF/text"
    DESCRIPTION = ("Load a .txt file and output its content as a string. "
                   "Use folder_path to pick a custom folder, or file_path to "
                   "directly specify the full path. If both are empty, falls "
                   "back to ComfyUI's default input directory.")

    @classmethod
    def VALIDATE_INPUTS(cls, **kwargs):
        # Allow manually typed file names / paths that are not in the
        # dropdown list. Actual existence is checked in main().
        return True

    def main(self, text_file, folder_path="", file_path=""):
        # 1) Highest priority: explicit full file path.
        if file_path and file_path.strip():
            text_file_path = file_path.strip()
        # 2) Manual folder: folder_path + text_file.
        elif folder_path and folder_path.strip():
            folder = folder_path.strip()
            if not os.path.isdir(folder):
                print(f"Error: The folder `{folder}` cannot be found.")
                return ("",)
            text_file_path = os.path.join(folder, text_file)
        # 3) Original behavior: ComfyUI default input directory.
        else:
            input_dir = folder_paths.get_input_directory()
            text_file_path = os.path.join(input_dir, text_file)

        if not os.path.exists(text_file_path):
            print(f"Error: The file `{text_file_path}` cannot be found.")
            return ("",)

        with open(text_file_path, "r", encoding="utf-8") as f:
            text = f.read()
        return (text,)


NODE_CLASS_MAPPINGS = {
    "TextLoadFile": TextLoadFile,
    "TextLoadFileAdvanced": TextLoadFileAdvanced,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextLoadFile": "TextLoadFile (Legacy)",
    "TextLoadFileAdvanced": "TextLoadFile Advanced",
}

# TextLoadFileCustom

Enhanced **TextLoadFile** node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI), based on the
node from [ClownsharkBatwing/RES4LYF](https://github.com/ClownsharkBatwing/RES4LYF).

The original node can only list `.txt` files inside ComfyUI's **default input directory** and gives
you no way to load a file from another folder. This project adds two new inputs so you can
**manually specify a folder or a full file path**.

## Features

- `TextLoadFile` — the original node, kept for backward compatibility.
- `TextLoadFileAdvanced` — adds two optional inputs:

  | Input | Type | Description |
  |-------|------|-------------|
  | `text_file` | dropdown / upload | Name of the `.txt` file (listed from the default input dir, or type any name manually). |
  | `folder_path` | STRING | Manually specify any folder on disk. The file is then read from `folder_path/text_file`. |
  | `file_path` | STRING | Directly specify the full path to a `.txt` file, bypassing the dropdown entirely. |

**Resolution priority:**

1. `file_path` (full path, highest priority)
2. `folder_path` + `text_file` (manual folder)
3. ComfyUI default input directory + `text_file` (original behavior)

If both `folder_path` and `file_path` are left empty, the node behaves exactly like the original.

## Installation

Put this folder inside your ComfyUI `custom_nodes` directory, then restart ComfyUI:

```
ComfyUI/custom_nodes/TextLoadFileCustom/
```

No extra dependencies are required.

## Usage example

1. Add the **TextLoadFile Advanced** node to your workflow.
2. Leave `text_file` empty (or pick anything from the dropdown).
3. Type the folder you want to read from into `folder_path`, e.g. `D:\prompts\styles`.
   - You may also type the exact file name in `text_file` even if it is not in the dropdown.
4. Run. The node reads `D:\prompts\styles\<text_file>` and outputs its content as a string.

Alternatively, put the complete path into `file_path` (e.g. `D:\prompts\styles\cyberpunk.txt`)
and it will be used directly.

## License

Same license as the upstream project ([RES4LYF](https://github.com/ClownsharkBatwing/RES4LYF)).

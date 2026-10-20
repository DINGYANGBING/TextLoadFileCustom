# TextLoadFileCustom

Enhanced **TextLoadFile** node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI), based on the
node from [ClownsharkBatwing/RES4LYF](https://github.com/ClownsharkBatwing/RES4LYF).

The original node can only list `.txt` files inside ComfyUI's **default input directory** and gives
you no way to load a file from another folder. This project adds two new inputs so you can
**manually specify a folder or a full file path**.

## Features

- `TextLoadFile` — the original node, kept for backward compatibility.
- `TextLoadFileAdvanced` — adds two optional inputs and a path output:

  | Input | Type | Description |
  |-------|------|-------------|
  | `text_file` | dropdown / upload | Name of the `.txt` file (listed from the default input dir). |
  | `folder_path` | STRING (text box) | Manually specify any folder on disk. The file is then read from `folder_path/text_file`. |
  | `file_path` | STRING (text box) | Directly specify the full path to a `.txt` file, bypassing the dropdown entirely. |

  | Output | Type | Description |
  |--------|------|-------------|
  | `text` | STRING | The loaded file content. |
  | `path` | STRING | The actual file path that was read. Use this to verify which folder was used. |

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
2. Pick any file in the `text_file` dropdown (its value will be the file name read from your custom folder).
3. Type the folder you want to read from into the `folder_path` text box, e.g. `D:\prompts\styles`.
4. Run. The node reads `D:\prompts\styles\<text_file>` and outputs its content. The `path` output shows the exact file that was read — check it to confirm the custom folder was used.

Alternatively, put the complete path into `file_path` (e.g. `D:\prompts\styles\cyberpunk.txt`)
and it will be used directly. This is also the way to load files that are NOT listed in
the `text_file` dropdown.

## License

Same license as the upstream project ([RES4LYF](https://github.com/ClownsharkBatwing/RES4LYF)).

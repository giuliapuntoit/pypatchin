# pypatch

Do you want a fast and clean solution to patch your files and repositories? Use me, a Python **pypatch** package!

I can patch your text, your files and your entire repositories!

To do so, I rely on the high performance patching library [diff-match-patch](https://github.com/google/diff-match-patch), making it accessible via Python code.

## How to use

Install requirements, setup, ...

See the ``try_me.py`` and ``check_me.py`` scripts.

## Examples

See the ``try_me.py`` and ``check_me.py`` scripts.

## Extras

Single text code

```
tmp_diff = compute_diff_from_strings("Test old text.", "Test new text.")
apply_diff_to_string("Text ole text", tmp_diff)
```

Single files code

```
compute_and_save_patch_from_file(original_dir_name, original_file_name, latest_dir_name, latest_file_name, patch_dir_name, patch_file_name)
apply_patch_to_file(original_dir_name, original_file_name, patch_dir_name, patch_file_name, patched_file_dir_name, patched_file_name)
```

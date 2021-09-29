from pypatch import patch_files


def main():

    # PATCH
    patch_dir_name = "patches/"

    # ORIGINAL
    original_dir_name = "original/"

    # LATEST
    latest_dir_name = "latest/"

    # GENERATED
    patched_file_dir_name = "generated/"

    # MULTIPLE FILES TO PATCH
    all_files_to_patch = ["each/file/you/wish.py",
                          "maybe/this.py",
                          "simple.py",
                          "README.md",
                          "each/"
                          ]

    # Generate patches for a list of files and apply them on original files
    patch_files.compute_and_save_patches_for_list_of_files(all_files_to_patch, original_dir_name, latest_dir_name, patch_dir_name)

    patch_files.apply_all_patches_to_files(all_files_to_patch, patch_dir_name, original_dir_name, patched_file_dir_name)


if __name__ == "__main__":
    main()

from pypatchin import compare


def main():
    latest_dir_name = "latest/"
    generated_dir_name = "generated/"

    all_files_to_patch = ["each/file/you/wish.py",
                          "maybe/this.py",
                          "simple.py",
                          "README.md",
                          "each/file.sh"
                          ]

    # Compare generated files and the version from which we patched
    result = compare.compare_latest_vs_generated_list_of_files(all_files_to_patch, latest_dir_name, generated_dir_name)
    print(result)

    # Result == True, files are equal
    # Result == False, files are different


if __name__ == "__main__":
    main()

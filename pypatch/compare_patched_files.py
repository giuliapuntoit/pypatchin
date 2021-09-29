from diff_match_patch import diff_match_patch


def read_file_to_text(file_path):
    file = open(file_path, "r")
    s = ''
    for line in file:
        s = s + line
    return s


def compare_latest_vs_generated_file(latest_dir, latest_file, generated_dir, generated_file):
    # Latest and generated files should be mostly equal

    # create diff string
    dmp = diff_match_patch()

    latest_path = latest_dir + latest_file
    generated_path = generated_dir + generated_file

    latest_text = read_file_to_text(latest_path)
    generated_text = read_file_to_text(generated_path)

    patches = dmp.patch_make(latest_text, generated_text)
    diff = dmp.patch_toText(patches)
    # print("DIFF \n######################")
    # print(diff)
    # print("LENGTH OF DIFF \n######################")
    # print(len(diff))

    if len(diff) == 0:
        return True
    else:
        return False


def compare_latest_vs_generated_list_of_files(list_of_files, latest_dir, generated_dir):
    for f in list_of_files:
        compare_latest_vs_generated_file(latest_dir, f, generated_dir, f)

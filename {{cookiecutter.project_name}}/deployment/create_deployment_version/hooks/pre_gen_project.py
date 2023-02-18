import os
import shutil


print("**********Pre Project Hook**************")


BASE_DIR = os.path.dirname(os.getcwd())

copy_from_src = False if "{{cookiecutter.copy_from_src_to_dist}}" == "NO" else True

if copy_from_src:
    src_dir = r"{{cookiecutter.src_dir|string}}".strip()

    src_dir_type = True
    if "{{cookiecutter.src_dir_type}}" == "Absolute":
        src_dir_type = False

    if src_dir_type:
        src_dir_path = os.path.join(BASE_DIR, src_dir)
    else:
        src_dir_path = os.path.join("", src_dir)

    src_dist_dir = r"{{cookiecutter.src_dist_dir|string}}".strip()

    src_dist_dir_type = True
    if "{{cookiecutter.src_dist_dir_type}}" == "Absolute":
        src_dist_dir_type = False

    if src_dist_dir_type:
        src_dist_dir_path = os.path.join(BASE_DIR, src_dist_dir)
    else:
        src_dist_dir_path = os.path.join("", src_dist_dir)

    print(
        f"Copy package src to dist folder from: '{src_dir_path}' to '{src_dist_dir_path}'"
    )

    # Clear Dist Folder
    for filename in os.listdir(src_dist_dir_path):
        filepath = os.path.join(src_dist_dir_path, filename)
        try:
            shutil.rmtree(filepath)
        except OSError:
            os.remove(filepath)

    shutil.copytree(
        src_dir_path,
        src_dist_dir_path,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns(
            *{{cookiecutter.copytree_ignore_patterns["ignore_patterns"]}}
        ),
    )

import os.path
import os
import shutil

print("**********Post Project Hook**************")

BASE_DIR = os.path.dirname(os.getcwd())

copy_from_dist = False if "{{cookiecutter.copy_from_src_dist}}" == "NO" else True

if copy_from_dist:
    src_dist_dir = r"{{cookiecutter.src_dist_dir|string}}".strip()

    src_dist_dir_type = True
    if "{{cookiecutter.src_dist_dir_type}}" == "Absolute":
        src_dist_dir_type = False

    if src_dist_dir_type:
        src_dist_dir_path = os.path.join(BASE_DIR, src_dist_dir)
    else:
        src_dist_dir_path = os.path.join("", src_dist_dir)

    print(f"Copy package dist folder from: '{src_dist_dir_path}'")

    package_dist_dir = "{{cookiecutter.project_slug}}/dist"
    package_dist_dir_path = os.path.join(BASE_DIR, package_dist_dir)

    shutil.copytree(src_dist_dir_path, package_dist_dir_path, dirs_exist_ok=True)

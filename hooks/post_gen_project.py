import os
import shutil


print("**********Post Project Hook**************")

BASE_DIR = os.path.dirname(os.getcwd())

clear_src = False if "{{cookiecutter.clear_src}}" == "NO" else True

if clear_src:
    src_dir = "{{cookiecutter.project_name}}/src/"
    src_dir_path = os.path.join(BASE_DIR, src_dir)

    print()
    print("cleared:")
    print(src_dir_path)
    print()

    for filename in os.listdir(src_dir_path):
        filepath = os.path.join(src_dir_path, filename)
        try:
            shutil.rmtree(filepath)
        except OSError:
            os.remove(filepath)

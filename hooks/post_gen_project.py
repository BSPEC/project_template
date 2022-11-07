import os
import shutil
import platform
import subprocess


print("**********Post Project Hook**************")


def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


BASE_DIR = os.path.dirname(os.getcwd())
clear_src = False if "{{cookiecutter.clear_src}}" == "NO" else True

src_dir = "{{cookiecutter.project_name}}/src/"
src_dir_path = os.path.join(BASE_DIR, src_dir)

if clear_src:

    for filename in os.listdir(src_dir_path):
        filepath = os.path.join(src_dir_path, filename)
        try:
            shutil.rmtree(filepath)
        except OSError:
            os.remove(filepath)
else:
    os.system('cd "' + src_dir_path + '" && python -m venv venv')
    os.system(
        'cd "'
        + src_dir_path
        + '" && venv/bin/activate && pip install --no-cache-dir -r requirements.txt'
    )
    os.system(
        'cd "'
        + src_dir_path
        + '" && venv\\Scripts\\activate && pip install --no-cache-dir -r requirements.txt'
    )
    ##################################################################################################
    # Repeat for python3 and pip3 as symlinks do not seem to work with os.system (at least on MacOS) #
    ##################################################################################################
    os.system('cd "' + src_dir_path + '" && python3 -m venv venv')
    os.system(
        'cd "'
        + src_dir_path
        + '" && venv/bin/activate && pip3 install --no-cache-dir -r requirements.txt'
    )
    os.system(
        'cd "'
        + src_dir_path
        + '" && venv\\Scripts\\activate && pip3 install --no-cache-dir -r requirements.txt'
    )

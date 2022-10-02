import os
import shutil
import json

from cookiecutter.main import cookiecutter

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

    print(f"Copy platform dist folder from: '{src_dist_dir_path}'")

    platform_dist_dir = f"{{cookiecutter.version}}/platform/dist"
    platform_dist_dir_path = os.path.join(BASE_DIR, platform_dist_dir)

    shutil.copytree(src_dist_dir_path, platform_dist_dir_path, dirs_exist_ok=True)


project_details_dir = "../project_details.json"
project_details_dir_path = os.path.join(BASE_DIR, project_details_dir)

project_details = open(project_details_dir_path)
project_details_data = json.load(project_details)

deployment_options_dir = "../deployment_options.json"
deployment_options_dir_path = os.path.join(BASE_DIR, deployment_options_dir)

deployment_options = open(deployment_options_dir_path)
deployment_options_data = json.load(deployment_options)

for template_directory_name in deployment_options_data["template_directory_names"]:
    # Should be cleaned for every template!
    extra_context_data = {}
    # We want the same basic project details for every project
    extra_context_data = project_details_data
    # This method of join will prioritize project details in case the template
    #  has the same values!
    extra_context_data |= deployment_options_data["template_directory_names"][
        template_directory_name
    ]

    cookiecutter(
        template="{{cookiecutter.deployment_options_template_dir}}",
        extra_context=extra_context_data,
        directory=template_directory_name,
        no_input=True,
        overwrite_if_exists=True,
        output_dir=f"platforms/{template_directory_name}/.",
    )

# Project Template
Project Template is designed to allow you to have a project src, dist and deployments (with versions). It is intended but not limited to be used with the [BSPEC Deployment Templates](https://github.com/BSPEC/deployment_templates)

## Notes:
This is part of the natural progression from the Flask-BDA project found here: [https://github.com/RyanJulyan/Flask-BDA](https://github.com/RyanJulyan/Flask-BDA) and should be considered it's successor.

## Requirements
------------
Install `cookiecutter` command line: 
```shell
pip install cookiecutter
pip install jinja2-ansible-filters

```

## Quickstart
------------
```shell
cookiecutter https://github.com/BSPEC/project_template

```

> Follow the prompts:
```shell
project_name [Project_Name]: Test
project_short_description [A short description of the project]: My Awesome description!
project_slug [test]:
Select clear_src:
1 - NO
2 - YES
Choose from 1, 2 [1]:

```

> This will create a new project with the name you provided in the prompt e.g. `Test`
> `cd` into the new project to see the files created:
```shell
cd Test

```

> Copy your project source files into `src`, and build for deployment into `dist`. this will allow you to use a single deployment repository and deploy to multiple platforms, using chosen strategies.

> Change the `deployment_options.json` to the deployment option details you wish to deploy to, default templates can be found at [https://github.com/BSPEC/deployment_templates](https://github.com/BSPEC/deployment_templates).
> By default all the values you require for all deployment `platform`_`stratergy`
> This is managed in `deployment_options.json` as `template_directory_names` since we are leveraging the cookie-cutter `directory` functionality for context when creating templates per `version` of the software you wish to deploy!

> Create a new version by `cd` into the deployment folder in your project, and then running the cookie-cutter create_deployment_version cmd
```shell
cd Test/deployment

cookiecutter create_deployment_version

```

> Follow the prompts:
```shell
version [0.0.1]:
Select src_dir_type:
1 - Relative
2 - Absolute
src_dir [../src]:
Select copy_from_src_to_dist:
1 - YES
2 - NO
Choose from 1, 2 [1]:
Select src_dist_dir_type:
1 - Relative
2 - Absolute
Choose from 1, 2 [1]:
src_dist_dir [../dist]:
Select copy_from_src_dist:
1 - YES
2 - NO
Choose from 1, 2 [1]:
deployment_options_template_dir [https://github.com/BSPEC/deployment_templates]:
copytree_ignore_patterns [default]:
```

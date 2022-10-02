# Project Template
Project Template is meant to allow you to have a project src, dist and deployments (with versions). It is meant to be used with the deployment_templates


## Requirements
------------
Install `cookiecutter` command line: 
```shell
pip install cookiecutter

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

```
```

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
src_dist_dir [../dist]:
Select copy_from_src_dist:
1 - YES
2 - NO
Choose from 1, 2 [1]:
Select src_dist_dir_type:
1 - Relative
2 - Absolute
Choose from 1, 2 [1]:
deployment_options_template_dir [https://github.com/BSPEC/deployment_templates]:
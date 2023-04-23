import os
import shutil
from jinja2 import Environment, FileSystemLoader, select_autoescape, StrictUndefined
from Models import *
import warnings
import black
import requests


class GenerateAPI:
    def __init__(self, local_file: bool = False):
        self.esi_schema = self.download_swagger_spec() if not local_file else self.local_swagger_spec()
        self.template_env = Environment(loader=FileSystemLoader("codegen/Templates"),
                                        autoescape=select_autoescape(),
                                        undefined=StrictUndefined)
        self.template_models: dict[str, ModelPath] = {}
        self.templates_rendered: dict[str, str] = {}
        self.total_templates_success = 0
        self.total_templates_fail = 0

    @classmethod
    def download_swagger_spec(cls, url: str = 'https://esi.evetech.net/latest/swagger.json') -> dict:
        print(f'Downloading latest swagger spec from {url}')
        r = requests.get(url, verify=True, timeout=60)
        r.raise_for_status()
        if r.status_code == 200:
            return r.json()
        else:
            raise Exception(f'Unexpected response code {r.status_code} when downloading ESI Swagger spec.')

    @classmethod
    def local_swagger_spec(cls):
        print(f'Loading local swagger spec from "swagger.json"')
        with open('swagger.json', 'r') as f:
            return json.load(f)

    def generate_template_models(self):
        for path_str, path in self.esi_schema['paths'].items():
            for method, d in path.items():
                try:
                    m = ModelPath.parse_swagger(self.esi_schema, d, path_str, method)
                    if m.class_name in self.templates_rendered:
                        raise Exception('Found duplicated model when all model names should be unique.')
                    self.template_models[m.class_name] = m
                except Exception as ex:
                    msg = f'Template generation for {method}->{path_str} was skipped due to exception: {ex}'
                    warnings.warn(msg)
                    self.total_templates_fail += 1

    def render_templates(self):
        for m in self.template_models.values():
            template_task = self.template_env.get_template('ESI_Task.py')
            rendered_task_module = template_task.render(m=m)
            rendered_task_module = black.format_str(rendered_task_module, mode=black.Mode(
                target_versions={black.TargetVersion.PY310},
                is_pyi=False,
                string_normalization=False
            ))
            package = m.package

            rendered_model_modules = {}
            template_models = self.template_env.get_template('ESI_Models.py')
            for response_success in m.responses_success:
                rendered_model = template_models.render(r=response_success, task_name=m.class_name)
                rendered_model = black.format_str(rendered_model, mode=black.Mode(
                    target_versions={black.TargetVersion.PY310},
                    is_pyi=False,
                    string_normalization=False
                ))
                module_name = f'{m.class_name}_{response_success.code}'
                rendered_model_modules[module_name] = rendered_model

            if not isinstance(self.templates_rendered.get(package), dict):
                self.templates_rendered[package] = {}
            if m.class_name in self.templates_rendered[package]:
                raise ValueError(f'Package cannot contain duplicated module names. "{m.class_name}" is duplicated')
            else:
                self.templates_rendered[package][m.class_name] = rendered_task_module

            if not isinstance(self.templates_rendered[package].get('Models'), dict):
                self.templates_rendered[package]['Models'] = {}
            for k, v in rendered_model_modules.items():
                if k in self.templates_rendered[package]['Models']:
                    raise ValueError(f'Package cannot contain duplicated module names. "{k}" is duplicated')
                else:
                    self.templates_rendered[package]['Models'][k] = v
            self.total_templates_success += 1

    def render_task_directory_templates(self):
        for package in list(self.templates_rendered.keys()):
            module_names_non_models = [k for k, v in self.templates_rendered.get(package, {}).items() if isinstance(v, str)]
            t = self.template_env.get_template('TaskDirectory.py')
            package_task_directory = t.render(package_name=package,
                                              module_names=module_names_non_models,
                                              module_models=self.template_models)
            package_task_directory = black.format_str(package_task_directory, mode=black.Mode(
                target_versions={black.TargetVersion.PY310},
                is_pyi=False,
                string_normalization=False
            ))
            self.templates_rendered[package]['TaskDirectory'] = package_task_directory
        t = self.template_env.get_template('RootTaskDirectory.py')
        root_task_directory = t.render(package_names=self.templates_rendered.keys())
        root_task_directory = black.format_str(root_task_directory, mode=black.Mode(
            target_versions={black.TargetVersion.PY310},
            is_pyi=False,
            string_normalization=False
        ))
        self.templates_rendered['TaskDirectory'] = root_task_directory

    def write_files(self):
        task_base = 'EVECelery/tasks'
        task_esi_path = f'{task_base}/ESI'
        try:
            shutil.rmtree(task_esi_path)
        except FileNotFoundError as ex:
            if not os.path.isdir(task_base):
                print(f'Unable to find path {task_base} relative to to the current working directory. Ensure it exists.')
                raise ex
        os.mkdir(task_esi_path)
        with open(f'{task_esi_path}/__init__.py', 'w') as f:
            f.write('')
        for package, package_contents in self.templates_rendered.items():
            if isinstance(package_contents, dict):
                package_path = f'{task_esi_path}/{package}'
                os.mkdir(package_path)
                with open(f'{package_path}/__init__.py', 'w') as f:
                    f.write('')
                for module, module_contents in package_contents.items():
                    if isinstance(module_contents, str):
                        with open(f'{package_path}/{module}.py', 'w') as f:
                            f.write(module_contents)
                    elif isinstance(module_contents, dict):
                        os.mkdir(package_path + '/Models')
                        with open(f'{package_path}/Models/__init__.py', 'w') as f:
                            f.write('')
                        for model_name, model_contents in module_contents.items():
                            with open(f'{package_path}/Models/{model_name}.py', 'w') as f:
                                f.write(model_contents)
                    else:
                        raise TypeError(f'Unexpected type: {type(module_contents)}')
            elif isinstance(package_contents, str):
                with open(f'{task_esi_path}/{package}.py', 'w') as f:
                    f.write(package_contents)
            else:
                warnings.warn(f'Unknown type for writing files: {type(package_contents)}')

    def print_summary(self):
        print(f'Total templates written successfully: {self.total_templates_success}\n'
              f'Total templates that failed to render / skipped: {self.total_templates_fail}')

    @classmethod
    def run(cls, local_file: bool):
        g = cls(local_file)
        g.generate_template_models()
        g.render_templates()
        g.render_task_directory_templates()
        g.write_files()
        g.print_summary()

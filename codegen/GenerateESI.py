import os
import shutil
from jinja2 import Environment, FileSystemLoader, select_autoescape, StrictUndefined
from Models import *
import warnings
import black
import requests

class GenerateAPI:
    def __init__(self):
        self.esi_schema = self.get_swagger_spec()
        self.template_env = Environment(loader=FileSystemLoader("codegen/Templates"),
                                        autoescape=select_autoescape(),
                                        undefined=StrictUndefined)
        self.template_models: dict[str, ModelPath] = {}
        self.templates_rendered: dict[str, str] = {}
        self.total_templates_success = 0
        self.total_templates_fail = 0

    @classmethod
    def get_swagger_spec(cls, url: str = 'https://esi.evetech.net/latest/swagger.json') -> dict:
        try:
            r = requests.get(url, verify=True, timeout=60)
            r.raise_for_status()
            if r.status_code == 200:
                return r.json()
            else:
                raise Exception(f'Unexpected response code {r.status_code} when downloading ESI Swagger spec.')
        except Exception as ex:
            print(ex)
            warnings.warn('Error when downloading ESI Swagger spac. Falling back to loading local swagger.json if it exists.')
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
            t = self.template_env.get_template('ESI_Task.py')
            m_rendered = t.render(m=m)
            m_rendered = black.format_str(m_rendered, mode=black.Mode(
                target_versions={black.TargetVersion.PY310},
                is_pyi=False,
                string_normalization=False
            ))
            package = m.package
            if not isinstance(self.templates_rendered.get(package), dict):
                self.templates_rendered[package] = {}
            if m.class_name in self.templates_rendered[package]:
                raise ValueError(f'Package cannot contain duplicated class names. "{m.class_name}" is duplicated')
            else:
                self.templates_rendered[package][m.class_name] = m_rendered
                self.total_templates_success += 1

    def render_task_directory_templates(self):
        for package in list(self.templates_rendered.keys()):
            t = self.template_env.get_template('TaskDirectory.py')
            package_task_directory = t.render(package_name=package,
                                              module_names=self.templates_rendered.get(package, {}).keys(),
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
                    with open(f'{package_path}/{module}.py', 'w') as f:
                        f.write(module_contents)
            elif isinstance(package_contents, str):
                with open(f'{task_esi_path}/{package}.py', 'w') as f:
                    f.write(package_contents)
            else:
                warnings.warn(f'Unknown type for writing files: {type(package_contents)}')

    def print_summary(self):
        print(f'Total templates written successfully: {self.total_templates_success}\n'
              f'Total templates that failed to render / skipped: {self.total_templates_fail}')

    @classmethod
    def run(cls):
        g = cls()
        g.generate_template_models()
        g.render_templates()
        g.render_task_directory_templates()
        g.write_files()
        g.print_summary()

from jinja2 import Environment, FileSystemLoader, select_autoescape, StrictUndefined
import json
from Models import *
import warnings
import black


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
    def get_swagger_spec(cls, url: str = None) -> dict:
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

    def print_summary(self):
        print(f'Total templates rendered successfully: {self.total_templates_success}\n'
              f'Total templates that failed to render / skipped: {self.total_templates_fail}')

    @classmethod
    def run(cls):
        g = cls()
        g.generate_template_models()
        g.render_templates()
        g.render_task_directory_templates()
        g.print_summary()

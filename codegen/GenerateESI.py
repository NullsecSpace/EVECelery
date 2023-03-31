from jinja2 import Environment, FileSystemLoader, select_autoescape, StrictUndefined
import json
from Models import *
import warnings


class GenerateAPI:
    def __init__(self):
        self.esi_schema = self.get_swagger_spec()
        self.template_env = Environment(loader=FileSystemLoader("codegen/Templates"),
                                        autoescape=select_autoescape(),
                                        undefined=StrictUndefined)
        self.template_models: list[ModelPath] = []
        self.templates_rendered: dict[str, str] = {}

    @classmethod
    def get_swagger_spec(cls, url: str = None) -> dict:
        with open('codegen/swagger.json', 'r') as f:
            return json.load(f)

    def generate_template_models(self):
        for path_str, path in self.esi_schema['paths'].items():
            for method, d in path.items():
                try:
                    m = ModelPath.parse_swagger(self.esi_schema, d, path_str, method)
                    self.template_models.append(m)
                except Exception as ex:
                    msg = f'Template generation for {method}->{path_str} was skipped due to exception: {ex}'
                    warnings.warn(msg)

    def render_templates(self):
        for m in self.template_models:
            t = self.template_env.get_template('ESI_Task.py')
            m_rendered = t.render(m=m)
            package = m.package
            if not isinstance(self.templates_rendered.get(package), dict):
                self.templates_rendered[package] = {}
            if m.class_name in self.templates_rendered[package]:
                raise ValueError(f'Package cannot contain duplicated class names. "{m.class_name}" is duplicated')
            else:
                self.templates_rendered[package][m.class_name] = m_rendered

    @classmethod
    def run(cls):
        g = cls()
        g.generate_template_models()
        g.render_templates()
        print('done')

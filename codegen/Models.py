from pydantic import BaseModel, validator, Field, conlist
import warnings
from typing import Literal
import json


def resolve_json_ref(full_dict: dict, input_dict: dict):
    if not isinstance(input_dict, dict):
        warnings.warn(f'{input_dict} is not a dictionary for resolve_json_ref')
    else:
        ref = input_dict.get('$ref')
        if ref:
            split_keys = ref.split('/')
            iter_dict = {}
            for k in split_keys:
                if k == '#':
                    iter_dict = full_dict
                else:
                    iter_dict = iter_dict[k]
            return iter_dict
        else:
            return input_dict


def extract_type(d: dict):
    d = d.get('schema', d)
    swagger_type = d.get('type')
    if swagger_type == 'array':
        return f'{swagger_type}[{extract_type(d.get("items"))}]'
    elif swagger_type == 'object':
        raise TypeError('not implemented yet')
    else:
        return swagger_type


class ModelProperty(BaseModel):
    name: str
    type: str
    paramLocation: str = ''
    description: str = 'No description available.'
    required: bool = False
    default_value: str | None = None

    @property
    def function_param(self):
        if self.default_value:
            if self.type == 'str':
                return f'{self.name}: {self.type} = "{self.default_value}"'
            else:
                return f'{self.name}: {self.type} = {self.default_value}'
        elif self.required:
            return f'{self.name}: {self.type}'
        else:
            return f'{self.name}: {self.type} | None = None'

    @property
    def param_pass(self):
        return f'{self.name}={self.name}'

    @property
    def function_docstring(self):
        return f':param {self.name}: {self.description}'

    @property
    def name_valid_python(self):
        return self.name.replace('-', '_')

    @property
    def name_alias(self) -> str | None:
        """
        returns an alias if the original name was invalid
        """
        if self.name != self.name_valid_python:
            return self.name
        else:
            return None

    @property
    def pydantic_field(self):
        alias = f', alias="{self.name_alias}"' if self.name_alias else ''
        if self.default_value:
            return f'{self.name_valid_python}: {self.type} = Field(default="{self.default_value}", description="{self.description}"{alias})'
        elif self.required:
            return f'{self.name_valid_python}: {self.type} = Field(default=..., description="{self.description}"{alias})'
        else:  # optional
            return f'{self.name_valid_python}: {self.type} | None = Field(description="{self.description}"{alias})'

    @validator('type', pre=True, always=True)
    def convert_to_python_type(cls, v):
        python_type_str = {
            'integer': 'int',
            'string': 'str',
            'boolean': 'bool',
            'array[integer]': 'list[int]',
            'array[array[integer]]': 'list[list[int]]',
            'array[string]': 'list[str]'
        }.get(str(v).casefold(), None)
        if python_type_str is None:
            raise ValueError(f"No mapping defined from ESI type '{v}' to Python type.")
        return python_type_str

    @property
    def pathParam(self):
        return 'path' in self.paramLocation.lower()

    @property
    def headerParam(self):
        return 'header' in self.paramLocation.lower()

    @classmethod
    def parse_swagger(cls, d: dict):
        return cls(name=d.get('name'),
                   type=extract_type(d),
                   paramLocation=d.get('in'),
                   description=(d.get('description', '') + ' -- ' + str(d.get('enum', ''))).rstrip('- '),
                   default_value=d.get('default'),
                   required=d.get('required', False)
                   )


class ModelResponse(BaseModel):
    code: int
    example: str = 'No example provided'
    description: str = 'No description provided'
    body_properties: list[ModelProperty] = Field(default_factory=list)
    header_properties: list[ModelProperty] = Field(default_factory=list)

    @property
    def modelClassName(self):
        """
        class name of object to create
        """
        return f'SuccessResponse{self.code}'

    @classmethod
    def parse_swagger(cls, code: int, d: dict):
        headers_properties = []
        for p_name, p_dict in d.get('headers', {}).items():
            m = ModelProperty(name=p_name,
                              type=extract_type(p_dict),
                              description=p_dict.get('description')
                              )
            headers_properties.append(m)
        body_properties = []
        body_schema = d.get('schema', {})
        if body_schema.get('type') == 'object':
            for p_name, p_dict in body_schema.get('properties').items():
                m = ModelProperty(name=p_name,
                                  type=extract_type(p_dict),
                                  description=p_dict.get('description'),
                                  required=p_name in body_schema.get('required', [])
                                  )
                body_properties.append(m)
        elif body_schema.get('type') == 'array':
            m = ModelProperty(name='items',
                              type=extract_type(d),
                              description=body_schema.get('title')
                              )
            body_properties.append(m)
        else:
            raise TypeError(f"Unknown starting type {body_schema.get('type')}")

        return cls(code=code,
                   example=json.dumps(d.get('examples', {}).get('application/json', {}), indent=2),
                   description=d.get('description'),
                   header_properties=headers_properties,
                   body_properties=body_properties
                   )


class ModelPath(BaseModel):
    method: Literal['get', 'post', 'delete']
    class_name: str
    path: str
    summary: str = 'No summary provided.'
    description: str = 'No description provided.'
    default_cache_ttl: int
    parameters: list[ModelProperty] = Field(default_factory=list, description='Input parameters to function call')
    responses_success: conlist(ModelResponse, min_items=1)
    tags: list[str] = Field(default_factory=list)

    @validator('default_cache_ttl', pre=True, always=True)
    def set_default_cache_ttl(cls, v):
        if v is None:
            return 60
        else:
            return v

    @property
    def package(self):
        """
        the package to place module in
        """
        return self.tags[0] if len(self.tags) >= 1 else 'uncategorized'

    @property
    def pathParams(self) -> list[ModelProperty]:
        return [p for p in self.requestParams if p.pathParam]

    @property
    def requestParams(self) -> list[ModelProperty]:
        params_no_default = []
        params_has_default = []
        for p in self.parameters:
            if not p.headerParam:
                if p.default_value or not p.required:
                    params_has_default.append(p)
                else:
                    params_no_default.append(p)
        return params_no_default + params_has_default

    @classmethod
    def parse_swagger(cls, full_swagger_dict: dict, path_dict: dict, path_str: str, method: str):
        # responses
        responses_success = []
        response_success_codes = [c for c in path_dict.get('responses').keys() if 200 <= int(c) < 300]
        if len(response_success_codes) == 0:
            raise ValueError('Expected at least one success response code')
        else:
            for success_code in response_success_codes:
                r = path_dict['responses'][success_code]
                responses_success.append(ModelResponse.parse_swagger(success_code, r))

        # inputs
        parameters = []
        for src_param_item in path_dict.get('parameters'):
            model_param = ModelProperty.parse_swagger(resolve_json_ref(full_swagger_dict, src_param_item))
            parameters.append(model_param)

        return cls(method=method,
                   class_name=path_dict.get('operationId'),
                   summary=path_dict.get('summary'),
                   description=path_dict.get('description'),
                   path=path_str,
                   tags=path_dict.get('tags'),
                   parameters=parameters,
                   responses_success=responses_success,
                   default_cache_ttl=path_dict.get('x-cached-seconds'))

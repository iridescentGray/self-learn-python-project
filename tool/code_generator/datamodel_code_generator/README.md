# datamodel-code-generator

Pydantic,dataclass generator for easy conversion of JSON, OpenAPI, JSON Schema, and YAML

## Environmental construction

### Used by pyenv virtualenv plugin

    pyenv virtualenv  3.10.11 datamodel-code-generator
    pyenv activate datamodel-code-generator
    python -m pip install --upgrade pip
    cd tool/datamodel-code-generator
    pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

## input/output

### input

- OpenAPI 3
- JSON Schema (JSON Schema Core/JSON Schema - Validation);
- JSON/YAML/CSV Data (it will be converted to JSON);
- Python dictionary (it will be converted to JSON);
- GraphQL schema

### output

- pydantic.BaseModel;
- pydantic_v2.BaseModel;
- dataclasses.dataclass;
- typing.TypedDict;
- msgspec.Struct;
- Custom type from your jinja2 template;

### Related documents

    datamodel-code-generator-doc： https://koxudaxi.github.io/datamodel-code-generator/
    datamodel-code-generator-github: https://github.com/koxudaxi/datamodel-code-generator

from pydantic import BaseModel, ConfigDict, ValidationError

# the full list of settings： https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict
print(f"-----------------------------------------limit_str_max_length ------------------------------------------")


class Model(BaseModel):
    model_config = ConfigDict(str_max_length=10)

    v: str


try:
    m = Model(v='x' * 20)
except ValidationError as e:
    print(e)

print(f"-----------------------------------------forbid extra field------------------------------------------")


class Model(BaseModel, extra='forbid'):
    a: str


try:
    Model(a='spam', b='oh no')
except ValidationError as e:
    print(e)

print(f"------------------------------global forbid extra field: use parent class-----------------------------------")


class Parent(BaseModel):
    model_config = ConfigDict(extra='forbid')


class Model(Parent):
    x: str


try:
    m = Model(x='foo', y='bar')
except ValidationError as e:
    print(e)

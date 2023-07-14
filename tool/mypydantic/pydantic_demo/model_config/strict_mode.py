from pydantic import BaseModel, ConfigDict, ValidationError

"""
By default, pydantic always open the Strict Mode
"""
print(f"-----------------------------------------strict mode open------------------------------------------")


class StrictModel(BaseModel):
    model_config = ConfigDict(strict=True)

    name: str
    age: int


strict_model1 = StrictModel(name="z", age=1)
print(strict_model1)

try:
    strict_model2 = StrictModel(name="z", age="2")
    print(strict_model2)
except ValidationError as e:
    print(e)

print(f"-----------------------------------------strict mode close------------------------------------------")


class UnStrictModel(BaseModel):
    model_config = ConfigDict(strict=False)

    name: str
    age: int


# No ValidationError Error
un_strict_model = UnStrictModel(name="z", age="2")
print(un_strict_model)

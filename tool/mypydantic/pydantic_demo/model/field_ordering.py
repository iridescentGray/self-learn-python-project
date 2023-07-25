from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    a: int
    b: int = 2
    c: int = 1
    d: int = 0
    e: float


print(f"------------------------------------Order For Field Dependent on ------------------------------------")

print(Model.model_fields.keys())
m = Model(e=2, a=1)
print(f"m.model_dump():{m.model_dump()}")
try:
    Model(a='x', b='x', c='x', d='x', e='x')
except ValidationError as err:
    error_locations = [e['loc'] for e in err.errors()]
    print(f"error_locations:{error_locations}")

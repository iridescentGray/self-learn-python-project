from pydantic import BaseModel, ConfigDict, ValidationError

# root model is the Way To Custom Definition Model
print(
    "-----------------------------------------immutability------------------------------------------"
)


class FooBarModel(BaseModel):
    model_config = ConfigDict(frozen=True)

    a: str
    b: dict


foobar = FooBarModel(a="hello", b={"apple": "pear"})

try:
    foobar.a = "different"
except ValidationError as e:
    print(e)

print(
    f"-----------------------------------nested field is not immutability------------------------------------------"
)

print(foobar.b)
foobar.b["apple"] = "grape"
print(foobar.b)

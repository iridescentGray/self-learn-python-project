from pydantic import BaseModel, create_model

print(
    f"----------------------------------------------Create Dynamic Model-------------------------------------------"
)
DynamicFoobarModel = create_model("DynamicFoobarModel", foo=(str, ...), bar=(int, 123))

dyFoobarBar = DynamicFoobarModel(foo="123", bar=11)
print(dyFoobarBar)

print(
    f"--------------------------------------------Create Base Other Model-----------------------------------------"
)


# __base__ can be used to make new model which includes extra fields.


class FooModel(BaseModel):
    foo: str
    bar: int = 123


BarModel = create_model(
    "BarModel",
    apple=(str, "russet"),
    banana=(str, "yellow"),
    __base__=FooModel,
)
# includes FooModel fields
print(BarModel.model_fields.keys())

from pydantic import BaseModel, InstanceOf, ValidationError


# use InstanceOf to check class type

class Fruit:
    def __repr__(self):
        return self.__class__.__name__


class Banana(Fruit):
    ...


class Apple(Fruit):
    ...


class Basket(BaseModel):
    fruits: list[InstanceOf[Fruit]]


print(Basket(fruits=[Banana(), Apple()]))
try:
    Basket(fruits=[Banana(), 'Apple'])
except ValidationError as e:
    print(e)

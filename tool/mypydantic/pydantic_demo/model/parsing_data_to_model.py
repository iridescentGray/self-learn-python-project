from datetime import datetime

from pydantic import BaseModel, ValidationError, ConfigDict

"""
Pydantic provides two classmethod helper functions on models for parsing data:
1.model_validate: this method except a dict arguments. 
                If the object passed is not a dict a ValidationError will be raised.
2.model_validate_json: this method takes a str or bytes, it will parses it as json, 
                     then passes the result to model_validate.
"""


class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime | None = None


print(f"-----------------------------------------dict parse------------------------------------------")

m = User.model_validate({'id': 123, 'name': 'James'})
print(m)

print(f"-----------------------------------------not a dict------------------------------------------")
try:
    User.model_validate(['not', 'a', 'dict'])
except ValidationError as e:
    print(e)

print(f"-----------------------------------------json parse------------------------------------------")

m = User.model_validate_json('{"id": 123, "name": "James"}')
print(m)

print(f"-----------------------------------------not valid json str------------------------------------------")
try:
    m = User.model_validate_json('{"id": 123, "name": 123}')
except ValidationError as e:
    print(e)

print(f"-----------------------------------------not json str------------------------------------------")

try:
    m = User.model_validate_json('Invalid JSON')
except ValidationError as e:
    print(e)


print(f"------------------------------------- nested data parse-----------------------------------")


class PetCls:
    def __init__(self, *, name: str, species: str):
        self.name = name
        self.species = species


class PersonCls:
    def __init__(self, *, name: str, age: float = None, pets: list[PetCls]):
        self.name = name
        self.age = age
        self.pets = pets


class Pet(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    species: str


class Person(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    pets: list[Pet]


bones = PetCls(name='Bones', species='dog')
orion = PetCls(name='Orion', species='cat')
anna = PersonCls(name='Anna', pets=[bones, orion])
anna_model = Person.model_validate(anna)
print(anna_model)

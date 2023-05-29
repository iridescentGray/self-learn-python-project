import logging

from pydantic import BaseModel, constr
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import declarative_base

logging.basicConfig(level=logging.INFO)


class User(BaseModel):
    id: int
    name = 'Jane Doe'


logging.info(f"-----------------------------------------Model Base Method------------------------------------------")
user = User(id=123)
logging.info(f"user: {user}")

logging.info(f"user.dict: {user.dict()}")
# json
logging.info(f"user.json: {user.json()}")
json_str = '{"id": 123, "name": "Jane Doe"}'
logging.info(f"user.parse_raw: {user.parse_raw(json_str)}")
# returns a dictionary representing the model as JSON Schema
# https://docs.pydantic.dev/latest/usage/schema/
logging.info(f"user.schema: {user.schema()}")
logging.info(f"user.schema_json: {user.schema_json()}")
# shallow_copy
user_shallow_copy = user.copy()
logging.info(f"user_shallow_copy: {user_shallow_copy}")
logging.info(f"user_shallow_copy is user: {user_shallow_copy is user}")
logging.info(f"user_shallow_copy == user: {user_shallow_copy == user}")
# Creating instance models without validation
logging.info(f"construct: {User.construct()}")
# Set of names of fields which were set when the model instance was initialised
logging.info(f"__fields_set__: {user.__fields_set__}")
logging.info(f"__fields__: {user.__fields__}")
# the configuration class for the model
# see https://docs.pydantic.dev/latest/usage/model_config/
logging.info(f"__config__: {user.__config__}")

logging.info(f"-----------------------------------------Recursive Models------------------------------------------")


# Python 3.10 and above
class Foo(BaseModel):
    count: int
    size: float | None = None


class Bar(BaseModel):
    apple = 'x'
    banana = 'y'


class Spam(BaseModel):
    foo: Foo
    bars: list[Bar]


recursive_spam = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
logging.info(f"recursive_spam: {recursive_spam}")
logging.info(f"recursive_spam: {recursive_spam.dict()}")

logging.info(f"------------------------------------- ORM-build_model_by_orm_class -----------------------------------")
Base = declarative_base()


class CompanyOrm(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    domains = Column(ARRAY(String(255)))


class CompanyModel(BaseModel):
    id: int
    public_key: constr(max_length=20)
    domains: list[constr(max_length=255)]

    class Config:
        # orm_mode must be set to True.
        orm_mode = True


co_orm = CompanyOrm(
    id=123,
    public_key='foobar',
    domains=['example.com', 'foobar.com'],
)
logging.info(f"co_orm: {co_orm}")
#  Used The special constructor from_orm to create the model instance.
company_model_from_orm = CompanyModel.from_orm(co_orm)
logging.info(f"CompanyModel.from_orm(co_orm): {company_model_from_orm}")

logging.info(f"------------------------------------- ORM-recursive_orm_models-----------------------------------")
from pydantic import BaseModel


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
    name: str
    species: str

    class Config:
        orm_mode = True


class Person(BaseModel):
    name: str
    age: float = None
    pets: list[Pet]

    class Config:
        orm_mode = True

bones = PetCls(name='Bones', species='dog')
orion = PetCls(name='Orion', species='cat')
anna = PersonCls(name='Anna', age=20, pets=[bones, orion])
anna_model = Person.from_orm(anna)
logging.info(f"anna_model.from_orm(anna): {anna_model}")

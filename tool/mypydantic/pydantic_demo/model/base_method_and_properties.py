from pydantic import BaseModel


# Model methods and properties: see  https://docs.pydantic.dev/latest/usage/models/#model-methods-and-properties
# Model Api: see https://docs.pydantic.dev/latest/api/main/#pydantic.main.BaseModel

class User(BaseModel):
    id: int
    name: str = 'Jane Doe'
    friends: list[int] = []


external_data = {
    "id": "123",
    "friends": [1, 2, "3"],
}

print(f"-----------------------------------------create instance------------------------------------------")
create_user_with_default_value = User(id=1, friends=[1, 2])
print(f"create_user_with_default_value:  {create_user_with_default_value}")
create_user_by_dict = User(**external_data)
print(f"create_user_by_dict:  {create_user_by_dict}")

print(f"----------------------------Create instance without validation-------------------------------------")
# Creating instance models without validation
print(f"model_construct: {User.model_construct()}")

print(f"-----------------------------------------dict----------------------------------------------")
user = User(id=123)
print(f"user: {user}")
print(f"dict view: user.model_dump: {user.model_dump()}")
print(f"dict view: user.model_dump: {type(user.model_dump())}")
print(f"-----------------------------------------json----------------------------------------------")
user_json = create_user_by_dict.model_dump_json()
print(f"user_json  {user_json}")
print(f"user_json object type {type(user_json)}")

# parse json to Object
json_str = '{"id": 123, "name": "Jane Doe"}'
user_from_json = User.model_validate_json(json_str)
print(f"user_from_json   {user_from_json}")
print(f"user_from_json object type  {type(user_from_json)}")

# 'is' return False, '==' return True, it means '== ' is overrider by pydantic
print(f"user is user_from_json  {create_user_by_dict is user_from_json}")
print(f"user==user_from_json  {create_user_by_dict == user_from_json}")

# returns a dictionary representing the model as JSON Schema
print(f"user.model_json_schema: {user.model_json_schema()}")

print(f"-------------------------------------------Model Shallow Copy---------------------------------------------")
# shallow_copy
user_shallow_copy = user.model_copy()
print(f"user_shallow_model_copy: {user_shallow_copy}")
print(f"user_shallow_model_copy is user: {user_shallow_copy is user}")
print(f"user_shallow_model_copy == user: {user_shallow_copy == user}")

print(f"--------------------------------------------properties-----------------------------------------------------")

# all fields
print(f"model_fields: {user.model_fields}")
# fields which were set when the model instance was initialized
print(f"user.model_fields_set: {user.model_fields_set}")
# fields set during validation
print(f"user.model_extra: {user.model_extra}")
# dictionary of the computed fields of this model instance
print(f"user.model_computed_fields: {user.model_computed_fields}")

# the configuration class for the model
# see https://docs.pydantic.dev/latest/usage/model_config/
print(f"__config__: {user.model_config}")

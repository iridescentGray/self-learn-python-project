from pydantic import BaseModel, TypeAdapter, ValidationError
from typing_extensions import TypedDict

"""
  Pydantic provides TypeAdapter,
  which can be used for type validation, serialization, and JSON schema generation without creating a BaseModel.

"""


class User(TypedDict):
    name: str
    id: int


print(
    "-------------------------------------------Best Way Conversion TypedDict To Dict -----------------------------------------"
)

user = User(name="123", id=1)
print(dict(user))


print(
    "-------------------------------------------Adapter TypedDict-----------------------------------------"
)


UserListValidator = TypeAdapter(list[User])
user_list = UserListValidator.validate_python(
    [{"name": "Fred", "id": "1"}, {"name": "Gray", "id": "2"}]
)
print(f"user_list {repr(user_list)}")

UserTypeAdapter = TypeAdapter(User)
print(f"type of UserTypeAdapter {repr(UserTypeAdapter)}")

user_validate_json = UserTypeAdapter.validate_json('{"id":123,"name":"Jane Doe"}')

# type is dict,not User
print("type of user_validate_json {type(user_validate_json)}")

print(
    "--------------------------------------Adapter TypedDict Validate Error-------------------------------------"
)

try:
    UserListValidator.validate_python([{"name": "Fred", "id": "wrong", "other": "no"}])
except ValidationError as e:
    print(e)

print(
    "------------------------------ parse into a type that is not subclass of BaseModel--------------------------"
)


class Item(BaseModel):
    id: int
    name: str


# a python data list like Item.class structure
item_data = [{"id": 1, "name": "My Item"}, {"id": 2, "name": "My Item2"}]

items = TypeAdapter(list[Item]).validate_python(item_data)
print(items)

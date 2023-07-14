print(f"---------------------------don't validate after create-------------------------------------------------")

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    name: str


user = User(name='John Doe')

print(user)
# don't validate after create
user.name = 123
print(user)

print(f"---------------------------keep validate after the model is created-----------------------------------")


class KeepValidateUser(BaseModel, validate_assignment=True):
    name: str


user = KeepValidateUser(name='John Doe')
print(user)
try:
    user.name = 123
except ValidationError as e:
    print(e)

print(f"----------------------------don't validate nested instance after transmit as param---------------------------")


class User(BaseModel, revalidate_instances='never'):
    hobbies: list[str]


class AlwaysValidateUser(BaseModel, revalidate_instances='always'):
    hobbies: list[str]


class SubUser(User):
    sins: list[str]


class Transaction(BaseModel):
    user: User | AlwaysValidateUser


my_user = User(hobbies=['reading'])
t1 = Transaction(user=my_user)
print(f"t1 {t1}")
my_user.hobbies = [1]
t2 = Transaction(user=my_user)
print(f"t2 {t2}")

print(f"---------------------------keep validate nested instance after transmit as param---------------------------")

always_validate_my_user = AlwaysValidateUser(hobbies=['reading'])
always_validate_my_user.hobbies = [1]
try:
    t3 = Transaction(user=always_validate_my_user)
    print(f"t3 {t3}")
except ValidationError as e:
    print(e)

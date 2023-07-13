from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name: str = "John Doe"
    friends: list[int] = []


print(f"------------------------------------------error_test-----------------------------------------------")
try:
    User(friends=[1, 2, "not number"])
except ValidationError as e:
    # A single exception of type ValidationError will be raised regardless of the number of errors found
    print(e)

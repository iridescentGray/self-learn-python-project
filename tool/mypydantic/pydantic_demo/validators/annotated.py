from typing import Annotated

from pydantic import BaseModel, ValidationError, field_validator
from pydantic.functional_validators import AfterValidator


def check_squares(v: int) -> int:
    assert v**0.5 % 1 == 0, f"{v} is not a square number"
    return v


def check_cubes(v: int) -> int:
    assert v ** (1 / 3) % 1 == 0, f"{v} is not a cubed number"
    return v


SquaredNumber = Annotated[int, AfterValidator(check_squares)]
CubedNumberNumber = Annotated[int, AfterValidator(check_cubes)]


class DemoModel(BaseModel):
    square_numbers: list[SquaredNumber] = []
    cube_numbers: list[CubedNumberNumber] = []

    # called before field validation
    @field_validator("square_numbers", "cube_numbers", mode="before")
    def split_str(cls, v):
        if isinstance(v, str):
            return v.split("|")
        return v

    @field_validator("cube_numbers", "square_numbers")
    def check_sum(cls, v):
        if sum(v) > 42:
            raise ValueError("sum of numbers greater than 42")
        return v


print(DemoModel(square_numbers=[1, 4, 9]))
print(DemoModel(square_numbers="1|4|16"))
print(DemoModel(square_numbers=[16], cube_numbers=[8, 27]))
try:
    DemoModel(square_numbers=[1, 4, 2])
except ValidationError as e:
    print(e)

try:
    DemoModel(cube_numbers=[27, 27])
except ValidationError as e:
    print(e)

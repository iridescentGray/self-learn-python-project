from typing import Annotated, TypeVar

from pydantic import BaseModel
from pydantic.functional_validators import AfterValidator

T = TypeVar("T")

SortedList = Annotated[list[T], AfterValidator(lambda x: sorted(x))]

Name = Annotated[str, AfterValidator(lambda x: x.title())]


class DemoModel(BaseModel):
    int_list: SortedList[int]
    name_list: SortedList[Name]


print(DemoModel(int_list=[3, 2, 1], name_list=["adrian g", "David"]))

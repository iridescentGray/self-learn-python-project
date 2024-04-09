from typing import Generic, TypeVar

from pydantic import BaseModel, ValidationError

# 泛型

print(
    "------------------------------------------------Create Generic--------------------------------------------"
)

DataT = TypeVar("DataT")


class DataModel(BaseModel):
    numbers: list[int]
    people: list[str]


class Response(BaseModel, Generic[DataT]):
    data: DataT | None = None


data = DataModel(numbers=[1, 2, 3], people=[])

print(Response[int](data=1))
print(Response[str](data="value"))
print(Response[DataModel](data=data).model_dump())

try:
    Response[int](data="value")
except ValidationError as e:
    print(e)

print(
    "------------------------------------------------Subclass Generic--------------------------------------------"
)
# To inherit from a generic model , subclass must also inherit from typing.Generic
TypeX = TypeVar("TypeX")


class BaseClassX(BaseModel, Generic[TypeX]):
    X: TypeX


class ChildClass(BaseClassX[TypeX], Generic[TypeX]):
    # must Inherit from Generic[TypeX]
    pass


print(ChildClass[int](X=1))

print(
    "------------------------------------------Subclass Change Generic------------------------------------------"
)
TypeA = TypeVar("TypeA")
TypeB = TypeVar("TypeB")
TypeC = TypeVar("TypeC")


class BaseClassAB(BaseModel, Generic[TypeA, TypeB]):
    a: TypeA
    b: TypeB


class ChildClassACB(BaseClassAB[int, TypeB], Generic[TypeB, TypeC]):
    c: TypeC


# Replace TypeB by str
print(ChildClassACB[str, int](a=1, b="y", c=3))

print(
    "---------------------------------------------Nested Generic--------------------------------------------------"
)
# Using the same TypeVar in nested models allows you to enforce typing relationships at different points in your model:
T = TypeVar("T")


class InnerT(BaseModel, Generic[T]):
    inner: T


class OuterT(BaseModel, Generic[T]):
    outer: T
    nested: InnerT[T]


print(OuterT[int](outer=1, nested=InnerT[int](inner=1)))
try:
    print(OuterT[int](outer="a", nested=InnerT[str](inner="a")))
except ValidationError as e:
    print(e)

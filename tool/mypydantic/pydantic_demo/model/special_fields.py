from datetime import datetime
from typing import ClassVar
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, PrivateAttr

print(
    "------------------------------------dynamic field values-------------------------------------"
)


class Model(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    updated: datetime = Field(default_factory=datetime.utcnow)


m1 = Model()
m2 = Model()
print(m1)
print(m2)

print(
    "------------------------------------Class Variables-------------------------------------"
)


class ClassModel(BaseModel):
    x: int = 2
    # use typing.ClassVar to definition a class variables
    y: ClassVar[int] = 1


m = ClassModel()
print(m)
print(ClassModel.y)

print(
    "------------------------------------Private Variables-------------------------------------"
)


class TimeAwareModel(BaseModel):
    _processed_at: datetime = PrivateAttr(default_factory=datetime.now)
    _secret_value: str


m = TimeAwareModel()
print(m._processed_at)

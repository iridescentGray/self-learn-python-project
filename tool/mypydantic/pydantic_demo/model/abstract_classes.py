import abc

from pydantic import BaseModel


class FooBarModel(BaseModel, abc.ABC):
    a: str
    b: int

    @abc.abstractmethod
    def my_abstract_method(self):
        pass


class SubClass(FooBarModel):
    def my_abstract_method(self):
        print(f"a: {self.a}, b:{self.b}")


sub_class = SubClass(a="my_a", b=1)
sub_class.my_abstract_method()

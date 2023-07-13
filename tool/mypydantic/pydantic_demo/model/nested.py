from pydantic import BaseModel

print(f"-----------------------------------------Recursive Models------------------------------------------")


class Foo(BaseModel):
    count: int
    size: float | None = None


class Bar(BaseModel):
    apple: str = 'x'
    banana: str = 'y'


class Spam(BaseModel):
    foo: Foo
    bars: list[Bar]


recursive_spam = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])

print(f"recursive_spam: {recursive_spam}")
print(f"recursive_spam: {recursive_spam.model_dump()}")
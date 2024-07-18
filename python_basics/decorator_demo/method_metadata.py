from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class Metadata:
    asset: Optional[str]
    flag: bool


def metadata_decorator(
    asset: str = "",
    *,
    flag: bool = False,
) -> Callable:
    """
    方法元数据装饰器
    """
    _asset = asset
    _flag = flag

    def decorator(fn):
        data = getattr(fn, "metadata", None)
        data = Metadata(_asset, _flag)
        setattr(fn, "metadata", data)
        return fn

    return decorator


class A:
    @metadata_decorator(asset="gogogo", flag=True)
    def test(self):
        return "hello"


if __name__ == "__main__":
    a = A()
    print(getattr(a.test, "metadata", None))  # Metadata(asset="gogogo", flag=True)

from typing import Annotated

from fast_depends import Depends, dependency_provider, inject


# this will be override
def abc_func() -> int:
    raise NotImplementedError()


def real_func() -> int:
    return 1


@inject
def func(dependency: Annotated[int, Depends(abc_func)]) -> int:
    return dependency


with dependency_provider.scope(abc_func, real_func):
    print(func())  # type: ignore

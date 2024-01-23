import asyncio
from fast_depends import inject, Depends


def sync_dependency(a: int) -> int:
    return a


@inject
def sync_main(a: int, b: int, c: int = Depends(sync_dependency)) -> float:
    return a + b + c


print(sync_main(1, 2))


async def asyncio_dependency(a: int) -> int:
    return a


@inject
async def asyncio_main(a: int, b: int, c: int = Depends(asyncio_dependency)) -> float:
    return a + b + c


print(asyncio.run(asyncio_main(1, 2)))

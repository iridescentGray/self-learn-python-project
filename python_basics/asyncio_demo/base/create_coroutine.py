import asyncio


async def coroutine_add_one(number):
    return number + 1


def add_one(number):
    return number + 1


function_result = add_one(1)
print(f"-----------------------------------------base function ------------------------------------------")

print(function_result)
print(type(function_result))

print(f"-----------------------------------------coroutine ------------------------------------------")
# Directly calling will only generate one coroutine object
coroutine_result = coroutine_add_one(1)
print(coroutine_result)
print(type(coroutine_result))

print(f"-----------------------------------------execute coroutine ------------------------------------------")

coroutine_result = asyncio.run(coroutine_add_one(1))
print(coroutine_result)
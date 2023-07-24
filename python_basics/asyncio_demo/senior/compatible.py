import asyncio


def commonly_function():
    print("I am a commonly function")


async def coroutine_function():
    print("I am a coroutine function")


print("---------------------------compatible_judge_function-------------------------------------")

print(f"commonly_function  iscoroutinefunction {asyncio.iscoroutinefunction(commonly_function)}")
print(f"coroutine_function  iscoroutinefunction {asyncio.iscoroutinefunction(coroutine_function)}")  # True

print(f"commonly_function  iscoroutine {asyncio.iscoroutine(commonly_function)}")
print(f"coroutine_function  iscoroutine {asyncio.iscoroutine(coroutine_function)}")

print(f"commonly_function()  iscoroutine {asyncio.iscoroutine(commonly_function())}")
print(f"coroutine_function()  iscoroutine {asyncio.iscoroutine(coroutine_function())}")  # True

print("----------------------------------judge_function_between_running------------------------------")


class TaskRunner:

    def __init__(self):
        self.loop = asyncio.new_event_loop()
        self.tasks = []

    def add_task(self, func):
        self.tasks.append(func)

    async def _run_all(self):
        awaitable_tasks = []

        for task in self.tasks:
            if asyncio.iscoroutinefunction(task):
                awaitable_tasks.append(asyncio.create_task(task()))
            elif asyncio.iscoroutine(task):
                awaitable_tasks.append(asyncio.create_task(task))
            else:
                # commonly_function
                self.loop.call_soon(task)

        await asyncio.gather(*awaitable_tasks)

    def run(self):
        self.loop.run_until_complete(self._run_all())


runner = TaskRunner()
runner.add_task(coroutine_function())
runner.add_task(coroutine_function)
runner.add_task(commonly_function)

runner.run()

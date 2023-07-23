import asyncio
from asyncio import Event


async def trigger_event(event: Event):
    await asyncio.sleep(3)
    event.set()


async def do_work_on_event(event: Event):
    print("wait event")
    await event.wait()  # if don't call event.set()，there will be a blockage here
    print("end")
    # Reset events，follow-up await event.wait() Will block again
    event.clear()


async def main():
    event = asyncio.Event()
    await asyncio.gather(trigger_event(event), do_work_on_event(event))


asyncio.run(main())

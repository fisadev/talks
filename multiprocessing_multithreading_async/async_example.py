from datetime import datetime
from random import randint
from asyncio import coroutine, sleep, Task, get_event_loop


info = []
results = []


async def generate_info():
    while True:
        await sleep(1)
        info.append(f"something at {datetime.now()}")
        print("New info added")


async def process_info():
    while True:
        await sleep(1)
        print("Checking for new info")
        if info:
            new_info = info.pop()
            results.append(new_info + "processed")
            print("New info processed")


loop = get_event_loop()
generator = loop.create_task(generate_info())
processor1 = loop.create_task(process_info())
processor2 = loop.create_task(process_info())
loop.run_forever()

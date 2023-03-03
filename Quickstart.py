# Phoebe Corwin
# 02 March 2023
# Using Asyncio in Python - Chapter 3: Quickstart.py

import asyncio
import time

#Patch found to prevent deprecation warning popup
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")


def blocking():
    time.sleep(0.5)
    print(f"{time.ctime()} Hello from a thread!")


loop = asyncio.get_event_loop()
task = loop.create_task(main())

loop.run_in_executor(None, blocking)
loop.run_until_complete(task)

pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()

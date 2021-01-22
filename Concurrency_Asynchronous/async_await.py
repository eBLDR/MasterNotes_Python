"""
Asynchronous programming is basically programming where execution order
is not known ahead of time (hence asynchronous instead of synchronous).
Concurrent programming is writing code to execute independently of other
parts (coroutines), it's all executed in a single thread.
Tasks release the CPU during waiting periods so that other tasks can use it,
when the task is completed, it will interrupt the main execution.
Asynchronous is used mostly when dealing with HTTP requests.

Asynchronous should be used when we do not need certain value for performing
other tasks:
    result = async_func()
    Do some additional work...
    data = await result;

It is of not use in the following case:
    result = await async_func()
"""
import asyncio
from random import randint


# async / await keywords, python 3.5+
# async - declaring a coroutine function
# Equivalent to @asyncio.coroutine
async def my_coroutine(id_):
    process_time = randint(1, 5)
    print(f'Coroutine {id_} - Working for {process_time} seconds...')

    # await - suspends the execution of coroutine on an awaitable object
    # It can only be used inside a coroutine function (async def ...)
    await asyncio.sleep(process_time)
    # Equivalent to yield from asyncio.sleep(delay)

    # asyncio.sleep(@seconds) is an awaitable, triggered after @seconds
    # asyncio.wait([@coroutines]) takes an iterable of coroutines tasks, will
    # return 2 sets
    # done, pending = yield from asyncio.wait([@coroutines])

    print(f'Coroutine {id_} - Task completed.')

    return process_time  # Coroutines can also have return value


# Creating the event loop - is a programming construct that waits for and
# dispatches events or messages in a program, it is the scheduler of tasks
loop = asyncio.get_event_loop()


async def msg(text):
    # Print with short sleep - for simulation purposes only
    await asyncio.sleep(0.1)
    print(text)


async def main():
    await msg('Before calling coroutine.')  # Chained to another function
    # create_task(@coroutine) - schedules the execution of a task, returns a
    # Task() object
    # create_task() python3.7- versions use ensure_future(@coroutine)
    task = asyncio.create_task(my_coroutine(0))
    await msg('After calling coroutine.')

    # Running a single task and storing the returned value (if desired)
    value = await task
    print('Task finished, value is:', value)


# Running a function from the event loop
loop.run_until_complete(main())

print('=' * 20)
input('Now let\'s run multiple times the same function... <enter>')


async def main_multiple():
    tasks = []
    for i in range(1, 8):
        tasks.append(asyncio.create_task(my_coroutine(i)))

    # Running multiple tasks - in a sequence
    value = await asyncio.gather(*tasks)
    print('All tasks finished, value is:', value)


loop.run_until_complete(main_multiple())

# Closing loop, to tidy up
loop.close()

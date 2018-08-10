"""
Asynchronous programming is basically programming where execution order
is not known ahead of time (hence asynchronous instead of synchronous).
Concurrent programming is writing code to execute independently of other
parts (coroutines), even if it all executes in a single thread.
"""
import asyncio

# New in Python 3.5 - async / await keywords

# async - declaring a coroutine function
async def countdown(countdown_seconds, delay):
    print('Waiting {} seconds before starting the countdown of {} seconds.'
          .format(delay, countdown_seconds))

    # await - suspends the execution of coroutine on an awaitable object
    # It can only be used inside a coroutine function (async def ...)
    await asyncio.sleep(delay)
    # asyncio.sleep(@seconds) is an awaitable, it will be triggered after the @seconds
    # asyncio.wait([@coroutines]) takes an iterable of coroutines tasks, will return 2 sets
    # done, pending = yield from asyncio.wait([@coroutines])
    
    print('Delay completed - starting countdown...')

    while countdown_seconds:
        print('\tCountdown - {} seconds left.'.format(countdown_seconds))

        await asyncio.sleep(1)

        countdown_seconds -= 1

    print('Countdown completed!')


# Creating the event loop - is a programming construct that waits for and
# dispatches events or messages in a program
loop = asyncio.get_event_loop()

print('I am calling countdown() function.')

# Running a function from the event loop
loop.run_until_complete(countdown(5, 2))

print('I have already called countdown() function.')

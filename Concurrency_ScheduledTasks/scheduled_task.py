# General purpose event scheduler
import sched
import time

from datetime import datetime


def print_time(arg='default'):
    print('From print_time: {}, w/ arg: {}.'.format(time.time(), arg))


def print_multiple_times():
    print('Starting print_multiple_times... {}'.format(time.time()))

    # Run after a lapse
    # enter(delay, priority, action, argument=(), kwargs={})
    my_event = scheduler.enter(7, 1, print_time)  # Return an event object
    scheduler.enter(3, 2, print_time, argument=('positional',))
    scheduler.enter(3, 1, print_time, kwargs={'arg': 'keyword'})

    print(my_event)

    # Run at a certain date/hour
    now = datetime.now()
    run_at = datetime(now.year, now.month, now.day, now.hour, now.minute, 55)

    # enterabs(time, priority, action, argument=(), kwargs={})
    # @time must be in seconds from epoch
    scheduler.enterabs(
        run_at.timestamp(), 1, print_time, argument=(
            'Running at ' + str(run_at),
        )
    )

    # cancel() - to cancel an event that's found in the queue
    # scheduler.cancel(my_event)

    # run() - run all scheduled events
    scheduler.run()

    # Return True if event queue is empty
    print('Queue is empty:', scheduler.empty())

    print('Finished print_multiple_times {}'.format(time.time()))


# scheduler(timefunc=time.monotonic, delayfunc=time.sleep)
# timefunc should be callable without arguments, and return a number (the
# time”, in any units whatsoever) delayfunc function should be callable with
# one argument, compatible with the output of timefunc
# If time.monotonic is not available, time.time will be the default
scheduler = sched.scheduler(time.time, time.sleep)

print('Calling print_multiple_times.\n')
print_multiple_times()
print('\nDone.')

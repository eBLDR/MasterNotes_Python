"""
Set handlers for asynchronous events.
The alarm counter starts in a parallel process.
"""
import signal
import sys

from time import sleep


def handler(*args):
    for arg in args:
        print(arg)

    signal_num = args[0]
    frame = args[1]

    print('Signal handler called with signal: {}.'.format(signal_num))

    sys.exit()


# signal.signal(signal.SIGALRM, f) - when alarm activated, f is called
# Only one alarm can be scheduled at any time
signal.signal(signal.SIGALRM, handler)

# Set the alarm's time in seconds
# It requests a SIGALRM to be sent to the process when time has passed
signal.alarm(3)

while True:
    print('Looping...')
    sleep(0.5)

signal.alarm(0)  # Disable the alarm, alarm is canceled

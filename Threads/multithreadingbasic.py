"""
A 'thread' is the execution of the code, line by line.
A 'single-threaded' program has only one thread of execution;
is reading and executing only one line at the time.
A 'multithreaded' program has multiple threads of execution (within one process);
is reading and executing multiple lines at the same time.

The module threading allows to implement this functionality.

With multiple threads, the program (the process) will finish when all of them have reached the
last line of its respective code. sys.exit() call will ONLY finish the
thread where the statement is found, not all the threads.

In most languages, each thread is assigned to one core, so two threads can run simultaneously,
but in Python, all threads are assigned to the same core of the process, making them not to run simultaneously.
"""

import threading
import time

print('Main Thread - Start.')


def take_nap():
    print('\nThread 1 - Start, Sleep!')
    time.sleep(5)
    print('\nThread 1 - End, Wake up!')


def print_(*args, **kwargs):
    print('\nThread 2 - Start, Print...')
    print(*args, **kwargs)
    print('\nThread 2 - End, Printed.')


def computing():
    print('\nThread 3 - Start, Counting...')
    j = 0
    for i in range(1000):
        j += i ** i
    print('\nThread 3 - End, Counted!')


# creating the thread object - target=function
thread_1 = threading.Thread(target=take_nap)
# starting of the execution of the target function in the new thread
thread_1.start()

# passing arguments to the thread's target function
my_args = ['Siamese Cat', 'Goldfish', 'Blue Jeans Frog']
thread_2 = threading.Thread(target=print_, args=my_args, kwargs={'sep': ' & '})
# args must be type iterable, if we wish to pass one single int, use (int,)
thread_2.start()

thread_3 = threading.Thread(target=computing)
thread_3.start()

print('\nMain Thread - End.')

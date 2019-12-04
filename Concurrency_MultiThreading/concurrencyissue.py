"""
Since all the threads are part of the same process, they share the namespace
(global variables), multiple threads can also cause problems called
'concurrency issues'.
These issues happen when threads read and write variables at the same time,
causing the threads to trip over each other.
Creating a new Thread object, make sure its target function uses only local
variables in that function.

If its necessary to manipulate the same variable from different threads (or
displaying in the screen), we can use a 'lock' object.
"""
import string
import threading
import time


def print_abc():
    # acquire() method locks the lock object - other threads cannot proceed
    # the execution until the lock is released
    print_lock.acquire()
    print('\n{} has locked the print_lock'.format(
        threading.current_thread().name
    ))

    # it can also work using a 'with' statement and deleting the acquire()
    # and release() calls
    # with print_lock:
    for char in string.ascii_uppercase:
        time.sleep(0.05)
        print(char, end='')

    # release() method unlocks the lock object - other threads can now proceed
    print_lock.release()
    print('\n{} has released the print_lock'.format(
        threading.current_thread().name
    ))


# this is the lock object - has two states: unlocked or locked
print_lock = threading.Lock()
print(type(print_lock))
print(print_lock)  # to see if it's unlocked or locked

for i in range(3):
    printer = threading.Thread(target=print_abc)
    printer.start()

print(print_lock)

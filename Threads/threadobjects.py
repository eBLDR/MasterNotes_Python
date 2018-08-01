"""
Different types of thread objects.
"""

import threading
import time


# TIMER OBJECTS - certain function will be executed after certain time
def salute():
    print('Ave Caesar!')


# timer.object(@seconds, @function) - function will be executed after @seconds from start() call
my_timer = threading.Timer(5, salute)
my_timer.start()  # here is where the timer starts

if input('Cancel timer [y/n] ? ').lower() == 'y':
    # to cancel the count and the execution
    my_timer.cancel()

# to wait executing main code until this thread is terminated
my_timer.join()

print("=" * 20)

# BARRIER OBJECTS - threads will wait for each other to be released
# @parties (int type) - number of threads to be blocked before releasing them
# @timeout (seconds) - time after which a BrokenBarrierError will be raised
my_barrier = threading.Barrier(2, timeout=10)


def server():
    time.sleep(3)
    print('Server active.')
    # wait() call sends one thread to the barrier - parties += 1
    # and wait for the barrier to have the number of specified parties before being released
    my_barrier.wait()


def client():
    print('Client active.')
    print('Waiting for server...')
    my_barrier.wait()
    print('Connection established.')


server_thread = threading.Thread(target=server)
client_thread = threading.Thread(target=client)

server_thread.start()
client_thread.start()

time.sleep(1)
# return the number of threads currently waiting in the barrier
print(my_barrier.n_waiting)

"""
abort() method - puts the barrier into a broken state.
This causes any active or future calls to wait() to fail with the BrokenBarrierError.

reset() method - return the barrier to the default, empty state.
Any threads waiting on it will receive the BrokenBarrierError exception.
"""

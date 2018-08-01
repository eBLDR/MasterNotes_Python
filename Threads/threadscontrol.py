import threading
import time


def counter(n, name):
    print(threading.current_thread())  # return the current thread object
    print('Counter {} - Start.'.format(name))
    time.sleep(n * 2)
    print('Counter {} - End.'.format(name))


# storing threads in a control list
my_threads = []

for x in range(1, 4):
    counting_thread = threading.Thread(target=counter, args=(x, str(x)))

    # adding thread to the thread's list
    my_threads.append(counting_thread)

    # starting the thread
    counting_thread.start()

# waiting for all threads to end
for thread in my_threads:
    # active_count() returns the number of threads currently alive (including the main thread)
    print('Number of threads alive: {}'.format(threading.active_count()))

    # enumerate() returns a list of all the threads currently alive (including daemon threads)
    print('List of threads alive: {}'.format(threading.enumerate()))

    # to get the name of the thread object (Thread-n)
    # equivalent to threading.current_thread().name
    who_is = thread.name

    # is_alive() method returns True if the thread is still executing and False if it has already terminated
    print('{} is alive: {}'.format(who_is, thread.is_alive()))

    # join() method will block/wait until the thread terminates
    thread.join()
    print('{} has finished.'.format(who_is))

    print('{} is alive: {}'.format(who_is, thread.is_alive()))

# From here, nothing will be executed until all the calls of the join() method have terminated
print('Threads alive: {}'.format(threading.active_count()))

print(threading.main_thread())  # Return the main thread object
                                # The main thread is the thread from which the Python interpreter was started

print('\nCounters done.')

print('\n', "=" * 30, '\n')

# Daemonic threads
daemon_test = threading.Thread(target=counter, args=(3, 'daemon'), daemon=False)  # Change to True to see difference
# The entire Python program exits when only daemon threads are left - it waits for all the
# non-daemonic threads to terminate

daemon_test.start()

print("Is {} a daemonic thread? {}".format(daemon_test.name, daemon_test.daemon))

if daemon_test.daemon:
    print('I am a demon, so the main thread is not waiting for me.')
else:
    print('I am not a daemon, the main thread IS waiting for me to end...')

print('\nMain thread has reached EOF.')

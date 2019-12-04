"""
Run from terminal.
When a process 'locks', the other processes will wait until the lock is
released.
"""
import logging
import multiprocessing
import os


def printer(item_, lock_):
    # Locking
    lock_.acquire()
    try:
        print('{} is printing: {}'.format(os.getpid(), item_))
    finally:
        # Unlocking
        lock_.release()


if __name__ == '__main__':
    # Lock object
    lock = multiprocessing.Lock()

    items = ['tango', 'foxtrot', 10]

    multiprocessing.log_to_stderr()  # To redirect to stderr pipe

    logger = multiprocessing.get_logger()  # Getting logger object
    logger.setLevel(logging.INFO)

    for item in items:
        p = multiprocessing.Process(target=printer, args=(item, lock))
        p.start()

"""
Run from terminal.
Pool represents a pool of worker processes.
Usually, the pool is run with a while loop inside, connected to a message queue,
and performing tasks whenever a message is received.
"""
from time import time
from multiprocessing import Pool


def costly_function(z):
    r = 0
    for k in range(1, 30000):
        r += z ** (1 / 2**k)
    return r


if __name__ == '__main__':
    data = [n for n in range(10)]

    # For performance example
    for workers in range(1, 6):

        # Pool is context manage, @processes = number of workers
        with Pool(processes=workers) as pool:
            start_time = time()
            
            # apply_async(f, (args,)) - evaluates f(arg) asynchronously in a single process
            # result is to be yield, not yet computed!
            result = pool.apply_async(costly_function, (2,))  # Result object

            # Computes the result with specifying timeout for evaluation,
            # if timeout expired, raises multiprocessing.TimeoutError
            print('result is: {}'.format(result.get(timeout=5)))

            # map_async(f, iter) - evaluates each item in iter in a single process
            result_2 = pool.map_async(costly_function, data)  # Returns an iterable result object
            print('result_2 is: {}'.format(result_2.get()))  # Iterates and computes the result object

            # pool.map(f, iter) returns a list with the results already computed

            print('\nIt took {} seconds for {} workers to get the job done.\n'
                  .format(time() - start_time, workers))

            # Prevents any more tasks from being submitted to the pool,
            # once all the tasks have been completed the worker processes will exit
            pool.close()

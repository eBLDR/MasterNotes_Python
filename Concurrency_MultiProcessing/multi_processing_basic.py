"""
Run from terminal.
Processes running on parallel.
"""
import os

from multiprocessing import Process, current_process


def square(n):
    r = n ** 2
    process_id = os.getpid()
    parent_process_id = os.getppid()
    name = current_process().name
    print('{0}**2 squared to {1} by process id {2} and name {3}, '
          'parent process is {4}'.format(
        n, r, process_id, name, parent_process_id)
    )


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    processes = []

    for index, number in enumerate(numbers):
        # Creating a process, target is the function to be triggered,
        # args is arguments (tuple)
        proc = Process(target=square, args=(number,), name='P-{}'.format(
            str(index)
        ))
        # Passing a specific @name

        processes.append(proc)

        # Daemon process - parent process will finish when ONLY non-daemon
        # processes are alive
        proc.daemon = True  # It's False by default

        # Start the execution of the process
        proc.start()

    for proc in processes:
        # Join tells to the main process to wait until the other processes
        # are finished
        proc.join()

        # proc.terminate() to kill a process

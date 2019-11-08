"""
Run from terminal.
Inter Process communication (IPC).
"""
import os

from multiprocessing import Pipe, Process


def f(conn, d):
    # Will send data to the other end of the pipe
    conn.send(d)
    print('Data {} sent from process {} to process {}.'
          .format(d, os.getpid(), os.getppid()))

    # Closing connection
    conn.close()


if __name__ == '__main__':
    # Pipe() returns a pair of connection objects connected by a pipe which
    # by default is duplex (two-way)
    parent_conn, child_conn = Pipe()

    data_to_be_sent = [42, None, 'hello']

    proc = Process(target=f, args=(child_conn, data_to_be_sent))
    proc.start()

    # Receiving data from the other end of the pipe
    data_received = parent_conn.recv()

    print('Process {} received data {}.'.format(os.getpid(), data_received))

    proc.join()

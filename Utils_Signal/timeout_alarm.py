"""
Create a timeout class for encapsulating blocks of code.
"""
import signal

from time import sleep


def test_request(arg=None):
    """ Any http request. """
    sleep(2)
    return arg


class Timeout:
    """ Timeout class context manager using ALARM signal. """

    # Customizing own exception
    class Timeout(Exception):
        pass

    def __init__(self, sec):
        self.sec = sec

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)

    def __exit__(self, *args):
        signal.alarm(0)  # Disable alarm

    def raise_timeout(self, *args):
        raise Timeout.Timeout()


if __name__ == '__main__':
    # Run block of code with different timeouts
    try:
        with Timeout(3):
            print(test_request('Request 1'))

        with Timeout(1):
            print(test_request('Request 2'))

    except Timeout.Timeout:
        print('Timeout!')

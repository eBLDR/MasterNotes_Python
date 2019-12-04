"""
While this script is running, use
$ kill -<INT> <PID>
to send signals to the current script.
"""
import signal
import os
from time import sleep


# Defining the handler
def receive_signal(signum, frame):
    # Each signal object has 2 attributes, signalnum (int) and frame (frame)
    print('Received: {}'.format(signum))


def immortal(signum, frame):
    # Handler for SIGHUP (kill process) signal
    receive_signal(signum, frame)
    print('YOU CANNOT KILL ME!')


# Registering handlers
signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)
signal.signal(signal.SIGHUP, immortal)

# SIGKILL and SIGSTOP cannot be handled
# signal.signal(signal.SIGKILL, immortal)

# Ignoring a signal, registering SIG_IGN handler
# SIGINT is the signal sent by pressing Ctrl+C (Keyboard Interrupt)
signal.signal(signal.SIGINT, signal.SIG_IGN)

# To see the registered signal handlers
print('SIGUSR1 has registered:', signal.getsignal(signal.SIGUSR1))
print('SIGUSR2 has registered:', signal.getsignal(signal.SIGUSR2))
print('SIGHUP has registered:', signal.getsignal(signal.SIGHUP))
print('SIGALRM has registered:', signal.getsignal(signal.SIGALRM))
print('SIGINT has registered:', signal.getsignal(signal.SIGINT))

print('=' * 30)

# Display process ID so it can be used with kill
print('My PID is: {}'.format(os.getpid()))

print('Paused. Send any signal to resume.')
# pause() - cause the process to sleep until a signal is received
signal.pause()

print('Waiting for either SIGUSR1 or SIGUSR2.')
# sigwait(sigset) - suspend execution of the calling thread until the delivery
# of one of the signals specified in the signal set sigset, the signal is
# removed from the list of signals, and returns the signal number.
signal.sigwait((signal.SIGUSR1, signal.SIGUSR2))

# Just wait for signal
while True:
    print('Waiting...')
    sleep(3)

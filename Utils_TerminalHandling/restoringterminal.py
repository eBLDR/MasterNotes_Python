"""
If while using curses the code raises an exceptions and stops,
the terminal won't be restore to it's original states,
since curses.endwin() was not called.
To avoid this issue, use wrapper.
"""
from curses import wrapper


def main(stdscr):
    stdscr.clear()

    # This raises a ZeroDivisionError
    for i in range(11, 0, -1):
        stdscr.addstr('10 divided by {} is {}'.format(i, 10/i))

    # If not the output will be erased when shifting back to original terminal
    stdscr.getkey()

"""
The wrapper() function takes a callable object and does the curses initialization,
wrapper() then runs the provided callable. Once the callable returns, wrapper()
will restore the original state of the terminal.
The callable is called inside a try…except that catches exceptions,
restores the state of the terminal, and then re-raises the exception.
Therefore your terminal will be left in the original state.
"""
wrapper(main)

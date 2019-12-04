"""
Displaying characters in custom way.
There are many attributes, but the compatibility depends
on the terminal being used.

Attribute	Description

A_BLINK	    Blinking text
A_BOLD	    Extra bright or bold text
A_DIM	    Half bright text
A_REVERSE	Reverse-video text
A_STANDOUT	The best highlighting mode available
A_UNDERLINE	Underlined text

Colors - curses initializes 8 basic colors

0   black
1   red
2   green
3   yellow
4   blue
5   magenta
6   cyan
7   white
"""
import curses


def main(stdscr):
    stdscr.clear()

    # Attributes
    stdscr.addstr('\nBlinking mode', curses.A_BLINK)
    stdscr.addstr('\nBold mode', curses.A_BOLD)
    stdscr.addstr('\nDim mode', curses.A_DIM)
    stdscr.addstr('\nReverse mode', curses.A_REVERSE)
    stdscr.addstr('\nStandout mode', curses.A_STANDOUT)
    stdscr.addstr('\nUnderline mode', curses.A_UNDERLINE)

    # Colors
    # curses.has_colors() returns True if terminal can display colors
    stdscr.addstr('\n\nHas colors: {}'.format(curses.has_colors()))

    # To use colors, we have to create a pair
    # init_pair(@pair_number, @foreground_color, @background_color)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    stdscr.addstr('\nRED ALERT!!', curses.color_pair(1))
    stdscr.addstr('\nSome info...', curses.color_pair(2))

    stdscr.getkey()


# wrapper() initializes colors automatically, if not, use curses.start_color()
curses.wrapper(main)

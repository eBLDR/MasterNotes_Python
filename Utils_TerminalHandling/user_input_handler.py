# curses module supplies a terminal-independent screen painting and
# keyboard-handling facility for text-based terminals.
import curses

# Initializing curses, gets setup for terminal
stdscr = curses.initscr()

while True:
    # Prints in stdout
    stdscr.addstr('using getch() - Press a key (q to quit): ')

    # Awaiting for a key to be pressed in stdin
    key = stdscr.getch()
    # getch() returns the unicode code for the key

    if key == ord('q'):
        # Exit loop if pressed key was 'q'
        break
    else:
        # Be careful with white characters (new line, space, tab...)
        stdscr.addstr('\nYou pressed: {}, which is {}\n'.format(key, chr(key)))


# Clear the screen
stdscr.clear()

while True:
    stdscr.addstr('using getkey() - Press a key (q to quit): ')

    key = stdscr.getkey()
    # getkey() is equivalent to getch() but converts the integer to a string
    # special characters have names such as 'KEY_UP'

    if key == 'q':
        # Exit loop if pressed key was 'q'
        break
    else:
        stdscr.addstr('\nYou pressed: {}\n'.format(key))

# Clear the screen
stdscr.clear()

while True:
    stdscr.addstr('using getstr() - Enter a string and press <enter> (quit): ')

    # Similar to input, editing keys available are backspace and Enter
    # String size can be limited to a fixed number of characters
    string = stdscr.getstr(10)
    # Returns a bytes type

    if string == b'quit':
        break
    else:
        stdscr.addstr('You typed: {}\n'.format(string))

# End curses and restore the terminal to its original operating mode
curses.endwin()

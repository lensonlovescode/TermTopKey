#!/usr/bin/env python3

import curses

class App():
    """
    Main application
    """
    def __init__(self):
        """
        The constructor method for the curses class
        """
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
    def start(self):
        """
        Initializes the curses mode, and takes over the screen
        """
    def window(self, height, width, y, x):
        """
        creates a new window
        """
        return cursees.newwin(height, width, y, x)

    def close(self):
        """
        Ends the curses mode
        """
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()


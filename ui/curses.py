#!/usr/bin/env python3
"""
Contains the curses module operations and start sequences as abstractions of an App class
"""
import curses


class App():
    """
    Main application
    """
    def __init__(self, stdscr):
        """
        The constructor method for the curses class.
        """
        self.stdscr = stdscr
        curses.noecho()
        curses.cbreak()

    def start(self):
        """
        The main loop of the application.
        """
        self.stdscr.clear()
        welcomemessage = "Welcome to TermTop keys, Press any key to continue or 'ctrl + x' to exit."
        center = (curses.COLS // 2) - (len(welcomemessage) // 2)
        self.stdscr.addstr(1, center, welcomemessage, curses.A_BOLD)
        self.stdscr.refresh()
        self.show_window()
        
        while True:
            key = self.stdscr.getch()
            if key == 24:
                break;
            else:
                self.show_window()

    def show_window(self):
        """
        Creates and shows a new window safely.
        """
        win = self.safe_window(0.9, 0.8, 0.1, 0.1)
        win.box()
        win.refresh()

    def safe_window(self, height_pct, width_pct, y_pct, x_pct):
        """
        Creates a window with dimensions and position as percentages of screen size,
        ensuring it never goes out of bounds.
        """
        max_h, max_w = self.stdscr.getmaxyx()
        h = int(max_h * height_pct)
        w = int(max_w * width_pct)
        y = int(max_h * y_pct)
        x = int(max_w * x_pct)

        if y + h >= max_h:
            y = max_h - h - 1
        if x + w >= max_w:
            x = max_w - w - 1
        
        y = max(0, y)
        x = max(0, x)

        return curses.newwin(h, w, y, x)

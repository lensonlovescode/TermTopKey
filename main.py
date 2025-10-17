#!/usr/bin/env python3
"""
Contains the entry point of the TUI application
"""
import curses
from ui.curses import App

def main(stdscr):
    """
    The entry point of the program, wrapped by curses.
    """
    app = App(stdscr)
    app.start()

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"An error occurred: {e}")

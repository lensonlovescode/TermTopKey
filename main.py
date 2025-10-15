#!/usr/bin/env python3
"""
Contains the entry point of the TUI application
"""
from ui import app

def main():
    """
    The entry point of the program
    """
    try:
        app.start()
        app.window()
    except:
        app.close()

if __name__ == "__main__":
    main()

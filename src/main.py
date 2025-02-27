import curses
from view.screenManager import ScreenManager

def main():
    screenManager = ScreenManager()
    screenManager.run()
    curses.endwin()

if __name__ == '__main__':
    main()
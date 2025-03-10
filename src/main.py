from __future__ import annotations
import curses
from view.screenManager import ScreenManager
import libs.configManager as configManager

def main(window:curses._CursesWindow):
    configManager.loadConfig("./config.json")
    screenManager = ScreenManager()
    screenManager.run(window)
    curses.endwin()
    configManager.saveConfig("./config.json")

if __name__ == '__main__':
    curses.wrapper(main)
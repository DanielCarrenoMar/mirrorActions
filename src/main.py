import curses
from view.screenManager import ScreenManager
import libs.configManager as configManager

def main():
    screenManager = ScreenManager()
    screenManager.run()
    curses.endwin()
    print(configManager.getConfig("text"))
    configManager.saveConfig("./config.json")

if __name__ == '__main__':
    main()
from screens.menuScreen import MenuScreen
from enum import Enum

class ScreenManager():
    class ScreenType(Enum):
        MENU = 1

    def __init__(self):
        self.screens = {
            self.ScreenType.MENU: MenuScreen()
        }
from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from view.screens.menuScreen import MenuScreen
from enum import Enum
from typing import Dict
from os import system

class ScreenManager():
    class ScreenType(Enum):
        MENU = 1

    def __init__(self):
        self.running = True
        self.screens:Dict[ScreenManager.ScreenType, BaseScreen] = {
            ScreenManager.ScreenType.MENU: MenuScreen(
                lambda: self.stop(),
                lambda: self.changeScreen(self.ScreenType.MENU),
                lambda: self.changeScreen(self.ScreenType.MENU),
                lambda: self.changeScreen(self.ScreenType.MENU)
            )
        }

        self.currentScreen = self.ScreenType.MENU

    def changeScreen(self, screen:ScreenManager.ScreenType):
        self.currentScreen = screen

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            curses.wrapper(self.screens[self.currentScreen].bucle)

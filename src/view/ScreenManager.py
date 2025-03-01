from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from view.screens.menuScreen import MenuScreen
from view.screens.finishScreen import FinishScreen
from view.screens.recordingScreen import RecordingScreen
from view.screens.saveAsScreen import SaveAsScreen
from enum import Enum
from typing import Dict
from os import system

class ScreenManager():
    class ScreenType(Enum):
        MENU = 1
        RECORDING = 2
        PLAYING = 3
        PLAY = 4
        PLAYOPTIONS = 5
        OPTIONS = 6
        SAVEAS = 7
        FINISH = 8
        DELETE = 9


    def __init__(self):
        self.running = True
        self.screens:Dict[ScreenManager.ScreenType, BaseScreen] = {
            ScreenManager.ScreenType.FINISH: FinishScreen(
                lambda: self.changeScreen(self.ScreenType.MENU),
                lambda: self.changeScreen(self.ScreenType.SAVEAS)
            ),

            ScreenManager.ScreenType.RECORDING: RecordingScreen(
                lambda: self.changeScreen(self.ScreenType.FINISH)
            ),

            ScreenManager.ScreenType.SAVEAS: SaveAsScreen(
                lambda: self.changeScreen(self.ScreenType.MENU),
            ),

            ScreenManager.ScreenType.MENU: MenuScreen(
                lambda: self.stop(),
                lambda: self.changeScreen(self.ScreenType.RECORDING),
                lambda: self.changeScreen(self.ScreenType.MENU),
                lambda: self.changeScreen(self.ScreenType.MENU)
            )
        }

        self.currentScreen = self.ScreenType.MENU

    def changeScreen(self, screen:ScreenManager.ScreenType):
        self.screens[self.currentScreen].hide()
        self.currentScreen = screen
        self.screens[self.currentScreen].show()

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            curses.wrapper(self.screens[self.currentScreen].bucle)

from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from view.screens.menuScreen import MenuScreen
from view.screens.finishScreen import FinishScreen
from view.screens.recordingScreen import RecordingScreen
from view.screens.playMenuScreen import PlayMenuScreen
from view.screens.playOptionsScreen import PlayOptionsScreen
from view.screens.playingScreen import PlayingScreen
from view.screens.saveAsScreen import SaveAsScreen
from enum import Enum
from typing import Dict

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
        CONFIG = 10

    def __init__(self):
        self.actionsList = []
        self.message = "Prueba"
        self.running = True

        self.screens:Dict[ScreenManager.ScreenType, BaseScreen] = {
            ScreenManager.ScreenType.FINISH: FinishScreen(
                lambda: self.changeScreen(self.ScreenType.MENU),
                lambda: self.changeScreen(self.ScreenType.SAVEAS)
            ),

            ScreenManager.ScreenType.RECORDING: RecordingScreen(
                lambda: self.changeScreen(self.ScreenType.SAVEAS),
                lambda message: self.changescreenWithMessage(self.ScreenType.MENU, message),
                self.setActionsList
            ),

            ScreenManager.ScreenType.SAVEAS: SaveAsScreen(
                lambda message: self.changescreenWithMessage(self.ScreenType.MENU, message),
                self.getActionsList
            ),

            ScreenManager.ScreenType.MENU: MenuScreen(
                self.stop,
                lambda: self.changeScreen(self.ScreenType.RECORDING),
                lambda: self.changeScreen(self.ScreenType.PLAY),
                lambda: self.changeScreen(self.ScreenType.CONFIG),
                self.getMessages,
                self.setMessages
            ),

            ScreenManager.ScreenType.PLAY: PlayMenuScreen(
                lambda message: self.changescreenWithMessage(self.ScreenType.MENU, message)
            )

        }

        """
        ScreenManager.ScreenType.PLAYOPTIONS: PlayOptionsScreen(

        ),

        ScreenManager.ScreenType.PLAYING: PlayingScreen(

        ),
        """

        self.currentScreen = self.ScreenType.MENU

    def getActionsList(self):
        return self.actionsList
    
    def setActionsList(self, actions:list):
        self.actionsList = actions

    def getMessages(self):
        return self.message
    
    def setMessages(self, message:str):
        self.message = message

    def changeScreen(self, screen:ScreenManager.ScreenType):
        self.screens[self.currentScreen].hide()
        self.currentScreen = screen
        self.screens[self.currentScreen].show()

    def changescreenWithMessage(self, screen:ScreenManager.ScreenType, message:str):
        self.message = message
        self.changeScreen(screen)

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            curses.wrapper(self.screens[self.currentScreen].bucle)

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
        self.message = ""
        self.bucles:int = 1
        self.running = True

        self.screens:Dict[ScreenManager.ScreenType, BaseScreen] = {
            ScreenManager.ScreenType.FINISH: FinishScreen(
                lambda: self.changeScreen(self.ScreenType.MENU),
                lambda: self.changeScreen(self.ScreenType.SAVEAS)
            ),

            ScreenManager.ScreenType.RECORDING: RecordingScreen(
                lambda: self.changeScreen(self.ScreenType.SAVEAS),
                lambda message: self.changeScreenWithMessage(self.ScreenType.MENU, message),
                self.setActionsList
            ),

            ScreenManager.ScreenType.SAVEAS: SaveAsScreen(
                lambda message: self.changeScreenWithMessage(self.ScreenType.MENU, message),
                self.getActionsList
            ),

            ScreenManager.ScreenType.MENU: MenuScreen(
                self.stop,
                lambda: self.changeScreen(self.ScreenType.RECORDING),
                lambda: self.changeScreen(self.ScreenType.PLAY),
                lambda: self.changeScreen(self.ScreenType.CONFIG),
                self.getMessage,
            ),

            ScreenManager.ScreenType.PLAY: PlayMenuScreen(
                lambda message: self.changeScreenWithMessage(self.ScreenType.MENU, message),
                lambda message: self.changeScreenWithMessage(self.ScreenType.PLAYOPTIONS, message),
                self.setActionsList
            ),

            ScreenManager.ScreenType.PLAYOPTIONS: PlayOptionsScreen(
                lambda: self.changeScreen(self.ScreenType.PLAY),
                lambda message: self.changeScreenWithMessage(self.ScreenType.PLAYING, message),
                lambda: self.changeScreen(self.ScreenType.DELETE),
                self.getMessage,
                self.getActionsList,
                self.getBucles,
                self.setBucles
            ),

            ScreenManager.ScreenType.PLAYING: PlayingScreen(
                lambda message: self.changeScreenWithMessage(self.ScreenType.MENU, message),
                self.getActionsList,
                self.getMessage,
                self.getBucles
            ),

        }

        self.currentScreen = self.ScreenType.MENU

    def getActionsList(self):
        return self.actionsList
    
    def setActionsList(self, actions:list):
        self.actionsList = actions

    def getMessage(self):
        return self.message
    
    def setMessages(self, message:str):
        self.message = message

    def getBucles(self) -> int:
        return self.bucles
    
    def setBucles(self, bucles:int):
        bucle = int(bucles)
        if bucle < 1: return
        self.bucles = bucles

    def changeScreen(self, screen:ScreenManager.ScreenType):
        self.screens[self.currentScreen].hide()
        self.currentScreen = screen
        self.screens[self.currentScreen].show()

    def changeScreenWithMessage(self, screen:ScreenManager.ScreenType, message:str):
        self.message = message
        self.changeScreen(screen)

    def stop(self):
        self.running = False

    def run(self, window:curses._CursesWindow):
        while self.running:
            self.screens[self.currentScreen].bucle(window)

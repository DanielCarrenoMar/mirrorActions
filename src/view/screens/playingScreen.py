from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from components.optionComp import OptionComp, OptionItemAction, OptionItemInput
import libs.configManager as configManager
from libs.playJsonKeys import Player, PlayerListener
from time import sleep
import threading

class PlayingScreen(BaseScreen, PlayerListener):
    def __init__(self, changeMenuWithMessage:callable, getActionsList:callable, getMessage:callable, getBucle:callable):
        super().__init__("Reproduciendo")
        self.getMessage = getMessage
        self.changeMenuWithMessage = changeMenuWithMessage
        self.getActionsList = getActionsList
        self.getBucle = getBucle
        self.actionIndex = 0
        
    def userInput(self, window, X, Y, text):
        pass

    def waitForStart(self):
        while self.waitTime > 0:
            sleep(1)
            self.waitTime -= 1
        self.player.play()
        self.changeMenuWithMessage("Reproducción finalizada")

    def show(self):
        self.player = Player(self.getActionsList(), configManager.getConfig("stopKeys"), self.getBucle())
        self.player.addListener(self)
        self.waitTime = 3
        threading.Thread(target=self.waitForStart).start()

    def onActionPlay(self, actionIndex):
        self.actionIndex = actionIndex

    def draw(self, window: curses._CursesWindow):
        super().draw(window)
        self.showMessage(window, self.getMessage() + f" Bucles:{self.getBucle()}")
        if self.waitTime > 0:
            window.addstr(2, 0, "Esperando " + str(self.waitTime) + " segundos para comenzar a grabar\n")
            return
        
        window.addstr(2,0, "Finalizar en " + str(configManager.getConfig("stopKeys")))
        
        for i, action in enumerate(self.getActionsList()[self.actionIndex:self.actionIndex + 10]):
            window.addstr(3 + i, 0, f"{self.actionIndex+i+1}. {action}")
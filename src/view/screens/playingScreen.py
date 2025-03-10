from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from components.optionComp import OptionComp, OptionItemAction, OptionItemInput
import libs.configManager as configManager
from libs.playJsonKeys import Player, PlayerListener
from time import sleep
import threading

class PlayingScreen(BaseScreen, PlayerListener):
    def __init__(self, changeMenuWithMessage:callable, getActionsList:callable, getMessages:callable):
        super().__init__("Reproduciendo")
        self.getMessages = getMessages
        self.changeMenuWithMessage = changeMenuWithMessage
        self.getActionsList = getActionsList
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
        self.player = Player(self.getActionsList(), configManager.getConfig("stopKeys"))
        self.player.addListener(self)
        self.waitTime = 3
        threading.Thread(target=self.waitForStart).start()

    def onActionPlay(self, actionIndex):
        self.actionIndex = actionIndex

    def draw(self, window: curses._CursesWindow):
        super().draw(window)
        window.addstr(0, 40 - len(self.getMessages()) ,self.getMessages())
        if self.waitTime > 0:
            window.addstr(2, 0, "Esperando " + str(self.waitTime) + " segundos para comenzar a grabar\n")
            sleep(.1)
            return
        
        window.addstr(2,0, "Finalizar en " + str(configManager.getConfig("stopKeys")) + "\n")
        
        for i, action in enumerate(self.getActionsList()[self.actionIndex:self.actionIndex + 10]):
            window.addstr(3 + i, 0, f"{self.actionIndex+i}. {action}")


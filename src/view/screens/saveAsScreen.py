from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from components.optionComp import OptionComp, OptionItemAction, OptionItemInput
import libs.configManager as configManager
from libs.saveJsonKeys import saveActions
from typing import Callable

class SaveAsScreen(BaseScreen):
    def __init__(self, changeMenu:callable, getActionsList:Callable[[], list]):
        super().__init__("Guardar Como")
        self.changeMenu = changeMenu
        self.getActionsList = getActionsList

    def userInputListener(self, input):
        actionsList = self.getActionsList()
        print("guardar " + str(actionsList))
        if len(actionsList) > 0:
            saveActions(actionsList, input)
            actionsList.clear()
        self.changeMenu()

    def inputLogic(self, window):
        userInputText = self.userInput(window, 0, 2, "Nombre: ")
        self.userInputListener(userInputText)

    def draw(self, window: curses._CursesWindow):
        super().draw(window)
        
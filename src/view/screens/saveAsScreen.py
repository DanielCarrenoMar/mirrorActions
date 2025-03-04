from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from components.optionComp import OptionComp, OptionItemAction, OptionItemInput
import libs.configManager as configManager
from libs.saveJsonKeys import saveActions
from typing import Callable

class SaveAsScreen(BaseScreen):
    def __init__(self, changeMenuWithMessage:Callable[[str], None], getActionsList:Callable[[], list]):
        super().__init__("Guardar Como")
        self.changeMenuWithMessage = changeMenuWithMessage
        self.getActionsList = getActionsList

        self.options = OptionComp(0, 3)
        self.options.addItem("0",OptionItemAction("Cancelar", self.changeMenuCancel))

    def changeMenuCancel(self):
        self.changeMenuWithMessage("Cancelado")

    def changeMenuSave(self, name):
        self.changeMenuWithMessage("Guardado como " + name)

    def userInputListener(self, input):
        if self.options.select(input): return

        actionsList = self.getActionsList()
        if len(actionsList) > 0:
            saveActions(actionsList, input)
            actionsList.clear()
        self.changeMenuSave(input)

    def inputLogic(self, window):
        userInputText = self.userInput(window, 0, 2, "Nombre: ")
        self.userInputListener(userInputText)

    def draw(self, window: curses._CursesWindow):
        super().draw(window)
        self.options.draw(window)
        
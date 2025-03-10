from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from components.optionComp import OptionComp, OptionItemAction, OptionItemInput
import libs.configManager as configManager
from typing import Callable

class PlayOptionsScreen(BaseScreen):
    def __init__(self, changePlayMenu:callable, changePlayingWithMessage:callable, changeDelete:callable, getMessage:callable, getActionsList:Callable[[None], list], getBucle:callable, setBucle:callable):
        super().__init__("reproducir")

        self.getMessage = getMessage
        self.getActionsList = getActionsList
        self.getBucle = getBucle

        self.options = OptionComp(0, 3)
        self.options.addItem("0",OptionItemAction("Cancelar", changePlayMenu))
        self.options.addItem("1",OptionItemAction("Iniciar", lambda: changePlayingWithMessage(getMessage())))
        self.options.addItem("2",OptionItemInput("Bucles", self.userInput, lambda input: setBucle(input)))
        self.options.addItem("3",OptionItemAction("Borrar", changeDelete))

    def userInputListener(self, input):
        self.options.select(input)

    def draw(self, window: curses._CursesWindow):
        super().draw(window)
        self.options.draw(window)
        window.addstr(0, 40 - len(self.getMessage()) ,self.getMessage())
        window.addstr(8, 0 , "Acciones:")
        for i,action in enumerate(self.getActionsList()[:4]):
            window.addstr(9 + i, 0, str(action))
            if i == 3: window.addstr("...")

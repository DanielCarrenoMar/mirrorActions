from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from components.optionComp import OptionComp, OptionItemAction, OptionItemInput
import libs.configManager as configManager

class SaveAsScreen(BaseScreen):
    def __init__(self, changeMenu:callable):
        super().__init__("Guardar Como")
        self.changeMenu = changeMenu

    def userInputListener(self, input):
        pass

    def draw(self, window: curses._CursesWindow):
        super().draw(window)
        
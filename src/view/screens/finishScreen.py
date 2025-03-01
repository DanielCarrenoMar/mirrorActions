from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from components.optionComp import OptionComp, OptionItemAction, OptionItemInput
import libs.configManager as configManager

class FinishScreen(BaseScreen):
    def __init__(self, changeMenu:callable, changeSaveAs:callable):
        super().__init__("Grabacion Finalizada")

        self.options = OptionComp(0, 3)
        self.options.addItem("0",OptionItemAction("Cancelar", changeMenu))
        self.options.addItem("1",OptionItemAction("Guardar", changeSaveAs))

    def userInputListener(self, input):
        self.options.select(input)

    def draw(self, window: curses._CursesWindow):
        super().draw(window)
        self.options.draw(window)
        
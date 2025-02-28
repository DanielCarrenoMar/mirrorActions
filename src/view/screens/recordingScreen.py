from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from components.optionComp import OptionComp, OptionItemAction, OptionItemInput
import libs.configManager as configManager

class RecordingScreen(BaseScreen):
    def __init__(self):
        super().__init__("Grabando...")

    def userInputListener(self, input):
        pass

    def inputLogic(self, window: curses._CursesWindow):
        pass

    def draw(self, window: curses._CursesWindow):
        super().draw(window)

        window.addstr("Finalizar en " + str(configManager.getConfig("endKeys")))

        
        
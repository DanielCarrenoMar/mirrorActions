from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from components.optionComp import OptionComp, OptionItemAction, OptionItemInput
import libs.configManager as configManager
from libs.recorderKeys import Recorder
from typing import Callable

class RecordingScreen(BaseScreen):
    def __init__(self, changeFinish:callable, setActionsList:Callable[[str], None]):
        super().__init__("Grabando...")
        self.changeFinish = changeFinish
        self.setActionsList = setActionsList
        self.recorder = None

    def userInputListener(self, input):
        pass

    def inputLogic(self, window: curses._CursesWindow):
        pass

    def stopHandler(self):
        self.setActionsList(self.recorder.getEvents())
        self.changeFinish()

    def show(self):
        self.recorder = Recorder(self.stopHandler, configManager.getConfig("endKeys"))
        self.recorder.start()

    def draw(self, window: curses._CursesWindow):
        super().draw(window)
        window.addstr("Finalizar en " + str(configManager.getConfig("endKeys")) + "\n")

        events = self.recorder.getEvents()
        for i, event in enumerate(reversed(events[-6:])):
            window.addstr(f"{i} - " + str(event) + "\n")
        self.recorder.wait()




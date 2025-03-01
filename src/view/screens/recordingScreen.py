from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from components.optionComp import OptionComp, OptionItemAction, OptionItemInput
import libs.configManager as configManager
from libs.recorderKeys import Recorder

class RecordingScreen(BaseScreen):
    def __init__(self, changeFinish:callable):
        super().__init__("Grabando...")
        self.changeFinish = changeFinish
        self.recorder = Recorder(self.stopHandler ,configManager.getConfig("endKeys"))

    def userInputListener(self, input):
        pass

    def inputLogic(self, window: curses._CursesWindow):
        pass

    def stopHandler(self):
        self.changeFinish()

    def show(self):
        self.recorder.start()

    def draw(self, window: curses._CursesWindow):
        super().draw(window)
        window.addstr("Finalizar en " + str(configManager.getConfig("endKeys")) + "\n")

        events = self.recorder.getEvents()
        for event in reversed(events[-3:]):
            window.addstr(str(event) + "\n")
        self.recorder.wait()


        
        
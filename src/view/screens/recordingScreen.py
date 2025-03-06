from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from components.optionComp import OptionComp, OptionItemAction, OptionItemInput
import libs.configManager as configManager
from libs.recorderKeys import Recorder
from time import sleep
import threading

class RecordingScreen(BaseScreen):
    def __init__(self, changeSaveAs:callable, changeMenuWithMessage:callable, setActionsList:callable):
        super().__init__("Grabando...")
        self.changeSaveAs = changeSaveAs
        self.changeMenuWithMessage = changeMenuWithMessage
        self.setActionsList = setActionsList
        self.recorder = None
        self.waitTime = None
        self.recording = False

    def userInputListener(self, input):
        pass

    def inputLogic(self, window: curses._CursesWindow):
        pass

    def stopHandler(self):
        if len(self.recorder.getEvents()) == 0:
            self.changeMenuWithMessage("No grabo ninguna accion")
            return

        self.setActionsList(self.recorder.getEvents())
        self.changeSaveAs()

    def waitForStart(self):
        while self.waitTime > 0:
            sleep(1)
            self.waitTime -= 1
        self.recording = True
        self.recorder.start()

    def show(self):
        self.waitTime = 3
        self.recorder = Recorder(self.stopHandler, configManager.getConfig("endKeys"))
        threading.Thread(target=self.waitForStart).start()

    def draw(self, window: curses._CursesWindow):
        super().draw(window)
        if self.waitTime > 0:
            window.addstr(2, 0, "Esperando " + str(self.waitTime) + " segundos para comenzar a grabar\n")
            sleep(.1)
            return

        window.addstr(2,0, "Finalizar en " + str(configManager.getConfig("endKeys")) + "\n")

        events = self.recorder.getEvents()
        for i, event in enumerate(reversed(events[-6:])):
            window.addstr(f"{i} - " + str(event) + "\n")
        self.recorder.wait()


        
        
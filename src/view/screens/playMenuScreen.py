from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from components.optionComp import OptionComp, OptionItemAction
from libs.saveJsonKeys import loadActions
from typing import Callable

class PlayMenuScreen(BaseScreen):
    def __init__(self, changeMenuWithMessage:Callable[[str],None], changePlayOptionsWithMessage:Callable[[str],None], setActionsList:Callable[[list],None]):
        super().__init__("reproducir")

        self.setActionsList = setActionsList
        self.changeMenuWithMessage = changeMenuWithMessage
        self.changePlayOptionsWithMessage = changePlayOptionsWithMessage

        self.options = OptionComp(0, 3)
            
    def show(self):
        self.options.clear()
        self.options.addItem("0",OptionItemAction("Salir", self.changeMenu))

        actions = loadActions()
        if len(actions) == 0: 
            self.changeMenuCancel()
            return
        
        for i, action in enumerate(actions):
            name = action['name']
            self.options.addItem(
                str(i + 1),
                OptionItemAction(
                    name,
                    lambda name=name, actionsList=action['actions']: self.changePlayOptionWithActionsList(name, actionsList)
                ))
            
    def changePlayOptionWithActionsList(self, name:str, actionsList:list):
        self.setActionsList(actionsList)
        self.changePlayOptionsWithMessage(name)

    def changeMenuCancel(self):
        self.changeMenuWithMessage("No hay acciones guardadas") 

    def changeMenu(self):
        self.changeMenuWithMessage("")

    def userInputListener(self, input):
        self.options.select(input)

    def draw(self, window: curses._CursesWindow):
        super().draw(window)
        self.options.draw(window)
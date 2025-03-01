from __future__ import annotations
import curses
from typing import Callable
from abc import abstractmethod
from components.component import Component

class OptionItem(Component):
    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def runAction(self):
        pass

class OptionItemAction(OptionItem):
    def __init__(self, text:str, action:callable):
        super().__init__(text)
        self.action = action

    def draw(self, window: curses._CursesWindow, X:int, Y:int):
        window.addstr(Y, X, self.text)

    def runAction(self):
        self.action()

class OptionItemInput(OptionItem):
    def __init__(self, text:str, userInputFun: Callable[[curses._CursesWindow, int, int, str],None], action:Callable[[str],None]):
        super().__init__(text)
        self.action = action
        self.editing = False
        self.userInputFun = userInputFun
        self.userInputText = ""
    
    def draw(self, window: curses._CursesWindow, X:int, Y:int):
        window.addstr(Y, X, self.text)
        if (not self.editing): return
        self.userInputText = self.userInputFun(window, X + len(self.text) + 1, Y, "")
        self.editing = False
        self.action(self.userInputText)

    def runAction(self):
        self.editing = True


class OptionComp():
    def __init__(self, X:int, Y:int):
        self.X = X
        self.Y = Y
        self.items:dict[str,OptionItem] = {}

    def addItem(self, key:str, item:OptionItem):
        self.items[key] = item

    def select(self, key:str):
        if (key not in self.items): return
        self.items[key].runAction()

    def draw(self, window: curses._CursesWindow):
        for i, (key,item) in enumerate(self.items.items()):
            window.addstr(self.Y + i, self.X, f"{key}. ")
            item.draw(window, self.X + len(key) + 2, self.Y + i)
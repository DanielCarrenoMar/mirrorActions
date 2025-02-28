from __future__ import annotations
import curses

class OptionItem():
    def __init__(self, text:str, action:callable):
        self.text = text
        self.action = action

    def draw(self, window: curses._CursesWindow, X:int, Y:int):
        window.addstr(Y, X, self.text)

    def action(self):
        self.action()

class OptionItemInput(OptionItem):
    def __init__(self, text:str, action:callable):
        super().__init__(text, action)

class OptionComp():
    def __init__(self, X:int, Y:int):
        self.X = X
        self.Y = Y
        self.items:dict[str,OptionItem] = {}

    def addItem(self, key:str, item:OptionItem):
        self.items[key] = item

    def select(self, key:str):
        if (key not in self.items): return
        self.items[key].action()

    def draw(self, window: curses._CursesWindow):
        for i, (key,item) in enumerate(self.items.items()):
            window.addstr(self.Y + i, self.X, f"{key}. ")
            item.draw(window, self.X + len(key) + 2, self.Y + i)
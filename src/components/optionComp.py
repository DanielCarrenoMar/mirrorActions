from __future__ import annotations
import curses

class OptionItem():
    def __init__(self, text:str, action:callable):
        self.text = text
        self.action = action

    def draw(self, window: curses._CursesWindow):
        window.addstr(self.text)

    def action(self):
        self.action()

class OptionComp():
    def __init__(self):
        self.items:dict[str,OptionItem] = {}

    def addItem(self, key:str, item:OptionItem):
        self.items[key] = item

    def select(self, key:str):
        if (key not in self.items): return
        self.items[key].action()

    def draw(self, window: curses._CursesWindow):
        for key ,item in self.items.items():
            window.addstr(f"{key}. ")
            item.draw(window)
            window.addstr("\n")
from __future__ import annotations
import curses
from components.component import Component

class HeaderComp(Component):
    def __init__(self, title:str):
        self.title = title

    def draw(self, window: curses._CursesWindow, X: int, Y: int):
        window.addstr(Y, X, f"{self.title.upper()} \n" +
            "----------------------------------------\n")

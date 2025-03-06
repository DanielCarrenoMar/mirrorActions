from __future__ import annotations
import curses
from components.headerComp import HeaderComp
from threading import Thread

class BaseScreen():
    def __init__(self, title:str):
        self.title = title
        self.header = HeaderComp(title)

    def userInput(self, window: curses._CursesWindow, X:int, Y:int, text:str) -> str:
        curses.echo()
        window.addstr(Y, X, text, curses.A_REVERSE)
        curses.flushinp()
        userInputText = window.getstr(Y, X + len(text) + 1, 10).decode('utf-8')
        curses.noecho()
        return userInputText

    def userInputListener(self, input):
        pass

    def show(self): pass

    def hide(self): pass

    def draw(self, window: curses._CursesWindow):
        self.header.draw(window, 0, 0)
        window.addstr("\n")

    def inputLogic(self, window: curses._CursesWindow):
        userInputText = self.userInput(window, 0, 2, "Opccion: ")
        self.userInputListener(userInputText)

    def bucle(self, window: curses._CursesWindow):
        window.clear()
        self.draw(window)
        self.inputLogic(window)
        window.refresh()
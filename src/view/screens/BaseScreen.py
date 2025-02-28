from __future__ import annotations
import curses
from components.headerComp import headerComp
from threading import Thread

class BaseScreen():
    def __init__(self, title:str):
        self.title = title

    def userInput(self, window: curses._CursesWindow, X:int, Y:int, text:str) -> str:
        curses.echo()
        window.addstr(Y, X, text, curses.A_REVERSE)
        userInputText = window.getstr(Y, X + len(text) + 1, 10).decode('utf-8')
        curses.noecho()
        return userInputText

    def userInputListener(self, input):
        pass

    def draw(self, window: curses._CursesWindow):
        headerComp(window,self.title)
        window.addstr("\n")

    def bucle(self, window: curses._CursesWindow):
        window.clear()
        self.draw(window)
        
        userInputText = self.userInput(window, 0, 2, "Opccion: ")
        self.userInputListener(userInputText)
        window.refresh()
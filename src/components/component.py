from __future__ import annotations
import curses
from abc import ABC, abstractmethod

class Component(ABC):
    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def draw(self, window: curses._CursesWindow, X: int, Y: int):
        pass
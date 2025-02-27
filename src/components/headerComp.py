from __future__ import annotations
import curses

def headerComp(window: curses._CursesWindow, title:str) -> str:
     
    window.addstr(f"{title.upper()} \n" +
            "----------------------------------------\n")

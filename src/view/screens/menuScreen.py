from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from components.optionComp import OptionComp, OptionItem

class MenuScreen(BaseScreen):
    def __init__(self, endApp:callable, changeRecording:callable, changePlay:callable, changeConfig:callable):
        super().__init__("Menu")

        self.options = OptionComp(0, 3)
        self.options.addItem("0",OptionItem("Salir", endApp))
        self.options.addItem("1",OptionItem("Grabar", changeRecording))
        self.options.addItem("2",OptionItem("Reproducir", changePlay))
        self.options.addItem("3",OptionItem("Configurar", changeConfig))

    def userInputListener(self, input):
        self.options.select(input)

    def draw(self, window: curses._CursesWindow):
        super().draw(window)
        self.options.draw(window)
        
        
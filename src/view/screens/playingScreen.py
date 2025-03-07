from __future__ import annotations
import curses
from view.screens.baseScreen import BaseScreen
from components.optionComp import OptionComp, OptionItemAction, OptionItemInput
import libs.configManager as configManager

class PlayingScreen(BaseScreen):
    def __init__(self, endApp:callable, changeRecording:callable, changePlay:callable, changeConfig:callable, getMessages:callable, setMessages:callable):
        super().__init__("Menu")

        self.getMessages = getMessages
        self.setMessages = setMessages

        self.options = OptionComp(0, 3)
        self.options.addItem("0",OptionItemAction("Salir", endApp))
        self.options.addItem("1",OptionItemAction("Grabar", changeRecording))
        self.options.addItem("2",OptionItemAction("Reproducir", changePlay))
        self.options.addItem("3",OptionItemAction("Configurar", changeConfig))

    def userInputListener(self, input):
        self.options.select(input)

    def draw(self, window: curses._CursesWindow):
        super().draw(window)
        self.options.draw(window)
        window.addstr(0, 40 - len(self.getMessages()) ,self.getMessages())
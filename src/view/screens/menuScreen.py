from src.view.screens import BaseScreen
from src.view.ScreenManager import ScreenManager

class MenuScreen(BaseScreen):
    def __init__(self, manager:ScreenManager, title:str):
        super().__init__(manager, title)
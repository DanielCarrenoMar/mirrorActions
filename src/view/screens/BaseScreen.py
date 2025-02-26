from src.view.ScreenManager import ScreenManager

class BaseScreen():
    def __init__(self, manager:ScreenManager, title:str):
        self.title = title
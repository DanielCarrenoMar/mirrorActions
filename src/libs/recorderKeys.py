from pynput.keyboard import Key, Listener, Controller
from pynput.mouse import Button, Controller
from pynput import mouse
from typing import Callable
from libs.configManager import getConfig
import threading

class Recorder:
    def __init__(self, stopFun:Callable[[], None], stopEvents = ["q"]):
        self.stopFun = stopFun
        self.stopEvents = stopEvents
        self.events = []
        self.mouseListener = mouse.Listener(on_click=self.onClick)
        self.keyboardListener = Listener(on_press=self.onPress)
    
    def onClick(self, x, y, button, pressed):
        print(x, y, button, pressed)
        if pressed:
            if button == Button.left:
                event = 'left_click' 
            elif button == Button.right:
                event = 'right_click'
            elif button == Button.middle:
                self.stop()
            self.events.append(["click",button, x, y])
            print(self.events )
            if event in self.stopEvents:
                self.stop()
    
    def onPress(self, key):
        keyStr = str(key).strip("'")
        self.events.append(["key", keyStr])
        if keyStr in self.stopEvents:
            self.stop()
    
    def start(self):
        self.mouseListener.start()
        self.keyboardListener.start()
        pass
    
    def stop(self):
        self.mouseListener.stop()
        self.keyboardListener.stop()
        self.stopFun()

    def wait(self):
        self.mouseListener.join(0.1)
        self.keyboardListener.join(0.1)
    
    def getEvents(self):
        return self.events
from pynput.keyboard import Listener
from pynput.mouse import Button
from pynput import mouse
from pynput.keyboard import Key, KeyCode
from typing import Callable
from time import time

class Recorder:
    def __init__(self, stopFun:Callable[[], None], stopEvents = ["q"]):
        self.stopFun = stopFun
        self.stopEvents = stopEvents
        self.events = []
        self.mouseListener = mouse.Listener(on_click=self.onClick)
        self.keyboardListener = Listener(on_press=self.onPress)
        self.lastEventTime = None
        self.started = False

    def calTimeBetween(self):
        if self.lastEventTime == None:
            self.lastEventTime = time()
            return 0

        currentTime = time()
        timeBetween = currentTime - self.lastEventTime
        self.lastEventTime = currentTime

        return timeBetween
    
    def onClick(self, x, y, button, pressed):
        if pressed:
            if button == Button.middle:
                self.stop()
                return

            self.events.append(
                {
                    "type":"click",
                    "key": str(button).lstrip("Button."), 
                    "X":x, 
                    "Y":y,
                    "time": self.calTimeBetween()
                }
            )

            """if event in self.stopEvents:
                self.stop()"""
    
    def onPress(self, key:Key | KeyCode):
        keyStr = str(key).strip("'")

        if keyStr in self.stopEvents:
            self.stop()
            return
        
        self.events.append(
                {
                    "type":"keyBoard",
                    "key": keyStr,
                    "time": self.calTimeBetween()
                }
            )
    
    def start(self):
        if self.started: return
        self.mouseListener.start()
        self.keyboardListener.start()
        self.started = True
            
    def stop(self):
        if not self.started: return
        self.mouseListener.stop()
        self.keyboardListener.stop()
        self.stopFun()
        self.started = False

    def wait(self):
        if not self.started: return
        self.mouseListener.join(0.1)
        self.keyboardListener.join(0.1)
    
    def getEvents(self):
        return self.events
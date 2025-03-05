from pynput.keyboard import Listener
from pynput.mouse import Button
from pynput import mouse
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
            if button == Button.left:
                event = 'left_click' 
            elif button == Button.right:
                event = 'right_click'
            elif button == Button.middle:
                self.stop()
                return

            self.events.append(
                {
                    "type":"click",
                    "key": str(button), 
                    "X":x, 
                    "Y":y,
                    "time": self.calTimeBetween()
                }
            )

            if event in self.stopEvents:
                self.stop()
    
    def onPress(self, key):
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
        self.mouseListener.start()
        self.keyboardListener.start()
            
    def stop(self):
        self.mouseListener.stop()
        self.keyboardListener.stop()
        self.stopFun()

    def wait(self):
        self.mouseListener.join(0.1)
        self.keyboardListener.join(0.1)
    
    def getEvents(self):
        return self.events
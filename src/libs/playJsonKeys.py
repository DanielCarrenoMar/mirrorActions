from abc import ABC, abstractmethod
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key
from pynput.mouse import Controller as MouseController, Button
from time import sleep
import json
from pynput import keyboard

deSerializeKeys = {
    "Key.space": Key.space,
    "Key.shift": Key.shift,
    "Key.ctrl": Key.ctrl,
    "Key.alt": Key.alt,
    "Key.cmd": Key.cmd,
    "Key.enter": Key.enter,
    "Key.esc": Key.esc,
    "Key.backspace": Key.backspace,
    "Key.caps_lock": Key.caps_lock,
    "Key.delete": Key.delete,
    "Key.down": Key.down,
    "Key.end": Key.end,
    "Key.f1": Key.f1,
    "Key.f2": Key.f2,
    "Key.f3": Key.f3,
    "Key.f4": Key.f4,
    "Key.f5": Key.f5,
    "Key.f6": Key.f6,
    "Key.f7": Key.f7,
    "Key.f8": Key.f8,
    "Key.f9": Key.f9,
    "Key.f10": Key.f10,
    "Key.f11": Key.f11,
    "Key.f12": Key.f12,
    "Key.f13": Key.f13,
    "Key.f14": Key.f14,
    "Key.f15": Key.f15,
    "Key.f16": Key.f16,
    "Key.f17": Key.f17,
    "Key.f18": Key.f18,
    "Key.f19": Key.f19,
    "Key.f20": Key.f20,
    "Key.home": Key.home,
    "Key.left": Key.left,
    "Key.page_down": Key.page_down,
    "Key.page_up": Key.page_up,
    "Key.right": Key.right,
}

class PlayerListener(ABC):
    @abstractmethod
    def onActionPlay(self, actionIndex:int):
        pass

class Player:
    def __init__(self, actions: list, stopKeys:list, bucles:int = 1, timeBetweenActions:float=None):
        self._keyboard = KeyboardController()
        self._mouse = MouseController()
        self._actions = actions
        self._listeners:list[PlayerListener] = []
        self._stop = False
        self._stopKeys = stopKeys
        self._bucles = bucles
        self._timeBetweenActions = timeBetweenActions

    def onPress(self, key):
        keyStr = str(key).strip("'")
        if keyStr in self._stopKeys:
            self._stop = True
            return False

    def play(self):
        listener = keyboard.Listener(on_press=self.onPress)
        listener.start()
        for _ in range(self._bucles):
            if self._stop:
                break
            for i, action in enumerate(self._actions):
                if self._stop:
                    break
                if self._timeBetweenActions: sleep(self._timeBetweenActions)
                else: sleep(action['time'])
                self.notify(i)
                if action['type'] == 'keyBoard':
                    key = action['key']
                    if key in deSerializeKeys: key = deSerializeKeys[key]
                    self._keyboard.press(key)
                    self._keyboard.release(key)
                elif action['type'] == 'click':
                    x, y = action['X'], action['Y']
                    self._mouse.position = (x, y)
                    if action['key'] == 'left':
                        self._mouse.click(Button.left)
                    elif action['key'] == 'right':
                        self._mouse.click(Button.right)
        listener.stop()

    def notify(self, actionIndex:int):
        for listener in self._listeners:
            listener.onActionPlay(actionIndex)

    def addListener(self, listener:PlayerListener):
        self._listeners.append(listener)

    def removeListener(self, listener:PlayerListener):
        self._listeners.remove(listener)

    def clearListeners(self):
        self._listeners.clear()

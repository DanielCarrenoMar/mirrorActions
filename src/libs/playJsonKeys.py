from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController, Button
from time import sleep
import json

keyboard = KeyboardController()
mouse = MouseController()

def playActions(actions: list):
    for action in actions:
        sleep(action['time'])
        if action['type'] == 'keyBoard':
            key = action['key']
            keyboard.press(key)
            keyboard.release(key)
        elif action['type'] == 'click':
            x, y = action['X'], action['Y']
            mouse.position = (x, y)
            if action['key'] == 'left':
                mouse.click(Button.left)
            elif action['key'] == 'right':
                mouse.click(Button.right)

def loadActions(filename: str) -> list:
    with open(filename, "r") as file:
        actions = json.load(file)
    return actions

# Example usage
filename = "saves/actions.json"
actions = loadActions(filename)
playActions(actions[0]['actions'])  # Replace 'example' with the actual key name

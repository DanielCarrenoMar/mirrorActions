import json
import os

def loadActions() -> list:
    if not os.path.exists("saves/actions.json"):
        return []

    with open("saves/actions.json", "r") as file:
        actions = json.load(file)

    return actions

def saveActions(actions: list, name: str):
    newActions = loadActions()

    newActions.append({name: actions})

    with open("saves/actions.json", "w") as file:
        file.write(json.dumps(newActions, indent=4))

    print("Guardado como " + name + ".json")
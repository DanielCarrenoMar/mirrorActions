import json
import os

def loadActions() -> list:
    if not os.path.exists("saves/actions.json"):
        return []

    with open("saves/actions.json", "r") as file:
        actions = json.load(file)

    return actions

def saveActions(actions: list, name: str) -> bool:
    newActions:list[dict[str,list]] = loadActions()

    for action in newActions:
        if action.get(name):
            return False

    newActions.append({"name": name, "actions": actions})

    if not os.path.exists("saves/"):
        os.makedirs("saves/")

    with open("saves/actions.json", "w") as file:
        file.write(json.dumps(newActions, indent=4))
    return True
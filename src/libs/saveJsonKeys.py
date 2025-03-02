import json

def saveActions(actions: list, name: str):
    if '.' in name:
        name = name.split('.')[0]

    with open("saves/" + name + ".json", "w") as file:
        file.write(json.dumps(actions))

    print("Guardado como " + name + ".json")
import json

config = {}

def updateConfig(key, value):
    global config
    config[key] = value

def getConfig(key):
    global config
    return config[key]

def loadConfig(file_path: str):
    global config
    with open (file_path) as json_file:
        config = json.load(json_file)

def saveConfig(file_path: str):
    global config
    with open(file_path, 'w') as json_file:
        json.dump(config, json_file, indent=4)

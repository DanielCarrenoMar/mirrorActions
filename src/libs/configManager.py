import json

config = {
    "endKeys": ["q", "2"]
}

def updateConfig(key, value):
    global config
    config[key] = value

def getConfig(key):
    global config
    return config[key]

def saveConfig(file_path: str):
    global config
    with open(file_path, 'w') as json_file:
        json.dump(config, json_file, indent=4)
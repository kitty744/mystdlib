from ..extras import json
from ..io import file

def load(path):
    return json.loads(file.read(path))

def save(path, data):
    file.write(path, json.dumps(data, indent=4))

def get(path, key, default=None):
    config = load(path)
    return config.get(key, default)

def set(path, key, value):
    try:
        config = load(path)
    except FileNotFoundError:
        config = {}

    config[key] = value
    save(path, config)
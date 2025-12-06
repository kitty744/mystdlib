import json
import pickle

def to_dict(obj):
    return obj.__dict__

def from_dict(cls, dict_obj):
    instance = cls.__new__(cls)
    instance.__dict__.update(dict_obj)
    return instance

def save_json(obj, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(to_dict(obj), f, indent=4)

def load_json(path, cls=None):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if cls:
        return from_dict(cls, data)
    return data

def save_binary(obj, path):
    with open(path, "wb") as f:
        pickle.dump(obj, f)

def load_binary(path):
    with open(path, "rb") as f:
        return pickle.load(f)
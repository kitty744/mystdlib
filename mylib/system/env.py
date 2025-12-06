import os as _os

def get(key, default=None):
    return _os.environ.get(key, default)

def set(key, value):
    _os.environ[key] = value

def all():
    return dict(_os.environ)

def has(key):
    return key in _os.environ

def remove(key):
    _os.environ.pop(key, None)
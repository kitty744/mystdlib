import os

def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def append(path, content):
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)

def exists(path):
    return os.path.exists(path)
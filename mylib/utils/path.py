import os as _os

def extname(path):
    return _os.path.splitext(path)[1]

def stem(path):
    return _os.path.splitext(_os.path.basename(path))[0]

def normalize(path):
    return _os.path.normpath(path)

def is_absolute(path):
    return _os.path.isabs(path)

def basename(path):
    return _os.path.basename(path)

def dirname(path):
    return _os.path.dirname(path)

def join(*paths):
    return _os.path.join(*paths)

def exists(path):
    return _os.path.exists(path)
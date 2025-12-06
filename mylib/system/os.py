import os as _os

def exists(path):
    return _os.path.exists(path)

def isfile(path):
    return _os.path.isfile(path)

def isdir(path):
    return _os.path.isdir(path)

def mkdir(path):
    return _os.mkdir(path)

def rmdir(path):
    return _os.rmdir(path)

def listdir(path):
    return _os.listdir(path)

def cwd():
    return _os.getcwd()

def chdir(path):
    return _os.chdir(path)

def join(a, b):
    return _os.path.join(a, b)

def basename(path):
    return _os.path.basename(path)

def dirname(path):
    return _os.path.dirname(path)
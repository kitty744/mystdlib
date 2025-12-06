import os as _os
import stat as _stat

def can_read(path):
    return _os.access(path, _os.R_OK)

def can_write(path):
    return _os.access(path, _os.W_OK)

def can_execute(path):
    return _os.access(path, _os.X_OK)

def is_file(path):
    return _os.path.isfile(path)

def is_dir(path):
    return _os.path.isdir(path)

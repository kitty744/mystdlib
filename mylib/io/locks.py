import threading as _threading
import os as _os
import platform as _platform
import tempfile as _tempfile

# -------------------------
# Platform imports
# -------------------------
try:
    import fcntl as _fcntl
except ImportError:
    _fcntl = None

try:
    import msvcrt as _msvcrt
except ImportError:
    _msvcrt = None


# -------------------------
# Thread Locks
# -------------------------

def create_lock():
    return _threading.Lock()

def acquire(lock):
    lock.acquire()

def release(lock):
    lock.release()

def try_acquire(lock, timeout=None):
    if timeout is None:
        return lock.acquire(blocking=False)
    return lock.acquire(timeout=timeout)


# -------------------------
# File Locks
# -------------------------

def lock_file(path):
    file = open(path, "a+")

    if _fcntl:
        _fcntl.flock(file.fileno(), _fcntl.LOCK_EX)
    elif _msvcrt:
        _msvcrt.locking(file.fileno(), _msvcrt.LK_LOCK, 1)
    else:
        raise RuntimeError("File locking not supported on this platform")
    
    return file

def unlock_file(file_object):
    if _fcntl:
        _fcntl.flock(file_object.fileno(), _fcntl.LOCK_UN)
    elif _msvcrt:
        _msvcrt.locking(file_object.fileno(), _msvcrt.LK_UNLCK, 1)

    file_object.close()


# -------------------------
# Process Locks
# -------------------------

_process_lock_dir = _tempfile.gettempdir()
_process_locks = {}

def acquire_process_lock(name):
    global _process_locks

    path = _os.path.join(_process_lock_dir, f"{name}.lock")

    file = open(path, "a+")

    if _fcntl:
        _fcntl.flock(file.fileno(), _fcntl.LOCK_EX)
    elif _msvcrt:
        _msvcrt.locking(file.fileno(), _msvcrt.LK_LOCK, 1)
    else:
        raise RuntimeError("Process locking not supported")
    
    _process_locks[name] = file
    return True

def release_process_lock(name):
    file = _process_locks.get(name)
    if not file:
        return False
    
    if _fcntl:
        _fcntl.flock(file.fileno(), _fcntl.LOCK_UN)
    elif _msvcrt:
        _msvcrt.locking(file.fileno(), _msvcrt.LK_UNLCK, 1)

    file.close()
    del _process_locks[name]
    return True
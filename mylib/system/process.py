import subprocess
import os
import signal

def run(command):
    return subprocess.run(command, shell=True, capture_output=True, text=True).stdout.strip()

def run_async(command):
    return subprocess.Popen(command, shell=True)

def kill(pid):
    try:
        os.kill(pid, signal.SIGTERM)
    except ProcessLookupError:
        pass

def exists(pid):
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False
import os as _os
import subprocess as _subprocess
import signal as _signal

def list_processes():
    if _os.name == "nt":
        output = _subprocess.check_output(["tasklist"])
    else:
        output = _subprocess.check_output(["ps", "-e"])

    return output.decode("utf-8").splitlines()

def kill_process(pid):
    if _os.name == "nt":
        _subprocess.run(["taskkill", "/PID", str(pid), "/F"], capture_output=True)
    else:
        try:
            _os.kill(pid, _signal.SIGTERM)
        except ProcessLookupError:
            pass

def is_running(pid):
    if _os.name == "nt":
        try:
            output = _subprocess.check_output(["tasklist", "/FI", f"PID eq {pid}"])
            return str(pid) in output.decode()
        except _subprocess.CalledProcessError:
            return False
    else:
        try:
            _os.kill(pid, 0)
            return True
        except ProcessLookupError:
            return False
        except PermissionError:
            return True

def start_process(command, args=None):
    full_command = [command] + args if args else [command]

    proc = _subprocess.Popen(
        full_command,
        stdout=_subprocess.PIPE,
        stderr=_subprocess.PIPE
    )

    return proc.pid
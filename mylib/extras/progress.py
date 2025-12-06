import time

_spinner_chars = "|/-\\"

def progress(current, total, length=30, prefix="", fill="#", empty=".", start_time=None, spinner_index=0):
    filled_length = int(length * current / total)
    bar = fill * filled_length + empty * (length - filled_length)

    percent = (current / total) * 100

    eta_str = ""
    if start_time is not None and current > 0:
        elapsed = time.time() - start_time
        eta = elapsed / current * (total - current)
        eta_str = f" ETA: {eta:.1f}s"

    spinner_char = _spinner_chars[spinner_index % len(_spinner_chars)]

    print(f"\r{prefix}{spinner_char} [{bar}] {percent:.1f}%{eta_str}", end="", flush=True)

    if current == total:
        print()
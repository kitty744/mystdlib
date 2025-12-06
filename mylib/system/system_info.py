import platform
import os
import sys
import shutil
import ctypes

# -----------------------------
# Operating System Info
# -----------------------------
def os_info():
    return {
        "name": platform.system(),
        "version": platform.version(),
        "architecture": platform.machine()
    }

# -----------------------------
# CPU Info
# -----------------------------
def cpu_info():
    return {
        "cores": os.cpu_count(),
        "architecture": platform.machine(),
        "processor": platform.processor()
    }

# -----------------------------
# Memory Info
# -----------------------------
def memory_info():
    system = platform.system()

    if system == "Linux":
        meminfo = {}
        with open("/proc/meminfo", "r") as f:
            for line in f:
                key, value = line.split(":")
                meminfo[key.strip()] = int(value.strip().split()[0])

        total = meminfo.get("MemTotal", 0) * 1024
        free = meminfo.get("MemFree", 0) * 1024
        available = meminfo.get("MemAvailable", free) * 1024

        return {
            "total": total,
            "free": free,
            "available": available,
            "used": total - free
        }

    elif system == "Windows":
        class MEMORYSTATUSEX(ctypes.Structure):
            _fields_ = [
                ("dwLength", ctypes.c_ulong),
                ("dwMemoryLoad", ctypes.c_ulong),
                ("ullTotalPhys", ctypes.c_ulonglong),
                ("ullAvailPhys", ctypes.c_ulonglong),
                ("ullTotalPageFile", ctypes.c_ulonglong),
                ("ullAvailPageFile", ctypes.c_ulonglong),
                ("ullTotalVirtual", ctypes.c_ulonglong),
                ("ullAvailVirtual", ctypes.c_ulonglong),
                ("sullAvailExtendedVirtual", ctypes.c_ulonglong)
            ]

        memoryStatus = MEMORYSTATUSEX()
        memoryStatus.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
        ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memoryStatus))

        return {
            "total": memoryStatus.ullTotalPhys,
            "available": memoryStatus.ullAvailPhys,
            "used": memoryStatus.ullTotalPhys - memoryStatus.ullAvailPhys
        }

    else:  # macOS or others
        try:
            import psutil
            mem = psutil.virtual_memory()
            return {
                "total": mem.total,
                "available": mem.available,
                "used": mem.used
            }
        except ImportError:
            return {"total": 0, "available": 0, "used": 0}

# -----------------------------
# Disk Info
# -----------------------------
def disk_info(path="/"):
    total, used, free = shutil.disk_usage(path)
    return {
        "total": total,
        "used": used,
        "free": free,
        "available": free
    }

# -----------------------------
# Python Info
# -----------------------------
def python_info():
    return {
        "version": sys.version,
        "version_info": tuple(sys.version_info),
        "implementation": platform.python_implementation(),
        "compiler": platform.python_compiler(),
        "build": platform.python_build(),
        "executable": sys.executable
    }

# -----------------------------
# Combined System Info
# -----------------------------
def full_system_info():
    return {
        "os": os_info(),
        "cpu": cpu_info(),
        "memory": memory_info(),
        "disk": disk_info(),
        "python": python_info()
    }

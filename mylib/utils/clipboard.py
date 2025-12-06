import tkinter as _tk

def copy(text):
    root = _tk.Tk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    root.destroy()

def paste():
    root = _tk.Tk()
    root.withdraw()
    text = root.clipboard_get()
    root.destroy()
    return text
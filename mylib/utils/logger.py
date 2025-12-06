from . import printer

def warn(message):
    printer.println("\033[93m[WARN]\033[0m " + message)

def error(message):
    printer.println("\033[91m[ERROR]\033[0m " + message)

def info(message):
    printer.println("\033[94m[INFO]\033[0m " + message)
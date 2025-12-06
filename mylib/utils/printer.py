import sys

def print(*args):
    output = ""

    for arg in args:
        output += str(arg) + " "

    sys.stdout.write(output.rstrip() + "\n")

def println(*args):
    output = ""

    for arg in args:
        output += str(arg) + " "
    sys.stdout.write(output.rstrip() + "\n")

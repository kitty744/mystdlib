import sys

def println(*args):
    output = ""

    for arg in args:
        output += str(arg)
        output += " "  # add space between arguments

    output += "\n"  # add a single newline at the end

    sys.stdout.write(output)

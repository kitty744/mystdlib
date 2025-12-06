from . import printer

def input(prompt=""):
    return __builtins__['input'](prompt)

def get_int(prompt, default=None):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            printer.println("Invalid integer. Try again.")
            if default is not None:
                return default
            
def get_float(prompt, default=None):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            printer.println("Invalid number. Try again.")
            if default is not None:
                return default
            
def get_choice(prompt, choices):
    choices_str = "/".join(str(c) for c in choices)
    while True:
        answer = input(f"{prompt} ({choices_str}): ")
        if answer in choices:
            return answer
        printer.println(f"Invalid choice. Pick one of: {choices_str}")
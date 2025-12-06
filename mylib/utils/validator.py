import re

def is_email(s):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, s))

def is_url(s):
    pattern = r"^https?://\S+\.\S+"
    return bool(re.match(pattern, s))

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_alpha(s):
    return s.isalpha()

def is_alnum(s):
    return s.isalnum()
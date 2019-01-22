import re

def echo(s):
    stripped = s.rstrip()
    sanitized = re.sub(r'  ', r' ', stripped)
    return sanitized

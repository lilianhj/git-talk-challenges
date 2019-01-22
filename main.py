def echo(s):
    sanitized = s.rstrip()
    if len(sanitized) > 2 and sanitized[0:2] != "  ":
        sanitized = "  " + sanitized
    return sanitized

import os


def line_break(s):
    if s is None:
        return s

    return s.replace("\\n", "\n")


def getenv_default(key, default=""):
    return os.getenv(key, default)

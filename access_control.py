# access_control.py


def compute_access_level(control, artist):
    return control * 3 + len(artist)


def validate_access(level, control):
    if level >= control * 5:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"


def audit_log(func):
    def wrapper(*args, **kwargs):
        print("    Authorization Started")
        result = func(*args, **kwargs)
        print("    Authorization Completed")
        return result

    return wrapper

import datetime
def make_readable(seconds):
    h = m = 0
    while seconds >= 3600:
        seconds -= 3600
        h += 1
    while seconds >= 60:
        seconds -= 60
        m += 1
    h = str(h).zfill(2)   
    m = str(m).zfill(2)
    s = str(seconds).zfill(2)
    return f"{h}:{m}:{s}"

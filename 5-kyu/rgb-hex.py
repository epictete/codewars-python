def limit(num):
    if num < 0:
        return 0
    elif num > 255:
        return 255
    else:
        return num

def rgb(r, g, b):
    r = ("%0.2X" % limit(r))
    g = ("%0.2X" % limit(g))
    b = ("%0.2X" % limit(b))
    return r + g + b

def rgb(r, g, b):
    r = 0 if r < 0 else r
    r = 255 if r > 255 else r
    r = ("%0.2X" % r)

    g = 0 if g < 0 else g
    g = 255 if g > 255 else g
    g = ("%0.2X" % g)

    b = 0 if b < 0 else b
    b = 255 if b > 255 else b
    b = ("%0.2X" % b)
    return r + g + b

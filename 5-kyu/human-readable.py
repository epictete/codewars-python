def make_readable(seconds):
    h, s = divmod(seconds, 3600)
    m, s = divmod(s, 60)
    return "{:02}:{:02}:{:02}".format(h, m, s)

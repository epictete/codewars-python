def generate_hashtag(s):
    if s == "" or len(s) > 140:
        return False
    else:
        arr = s.title().split()
        return "#" + "".join(arr)

def pig_it(text):
    arr = text.split()
    res = []
    for i in arr:
        if i.isalnum():
            i = i[1:] + i[0] + "ay"
        res.append(i)
    return " ".join(res)

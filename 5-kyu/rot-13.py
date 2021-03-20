def rot13(message):
    res = ""
    for i in message:
        if i.isalpha():
            if ord(i) >= 65 and ord(i) <= 77:
                i = chr(ord(i) + 13)
            elif ord(i) >= 78 and ord(i) <= 90:
                i = chr(ord(i) - 13)
            elif ord(i) >= 97 and ord(i) <= 109:
                i = chr(ord(i) + 13)
            elif ord(i) >= 110 and ord(i) <= 122:
                i = chr(ord(i) - 13)
        res += i
    return res

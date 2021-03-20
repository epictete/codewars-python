sample = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"

def ones(bits):
    print("one")
    stack = []
    max = 0
    for b in bits:
        if b == "1":
            stack.append(b)
        else:
            if len(stack) > max:
                max = len(stack)
            stack = []
    return int(max / 3) if max > 3 else 1

def zeroes(bits):
    stack = []
    max = 0
    for b in bits:
        if b == "0":
            stack.append(b)
        else:
            if len(stack) > max:
                max = len(stack)
            stack = []
    return int(max / 7) if max > 7 else 1

def decode_bits(bits):
    u = zeroes(bits)
    print(u)
    if u == 1:
        u = ones(bits)
    print(u)
    bits = bits.replace(u * "0", "0").replace(u * "1", "1")
    res = bits.replace('0000000', '   ').replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')
    return res

def decode_morse(morseCode):
    res = ""
    words = morseCode.split("   ")
    for word in words:
        tmp = ""
        letters = word.split()
        for letter in letters:
            tmp += MORSE_CODE[letter]
        res += tmp + " "
    return res.strip()


decode_bits(sample)
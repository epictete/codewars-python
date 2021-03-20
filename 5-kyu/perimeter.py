def perimeter(n):
    out = [1, 1]
    while len(out) - 1 < n:
        out.append(out[-1] + out[-2])
    return 4 * sum(out)

print(perimeter(7))
def solution(string,markers):
    lines = string.split("\n")
    res = []
    for line in lines:
        tmp = ""
        for char in line:
            if char in markers:
                break
            tmp += char
        res.append(tmp.strip())
    return "\\n".join(res)


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
print(solution("a #b\nc\nd $e f g", ["#", "$"]))
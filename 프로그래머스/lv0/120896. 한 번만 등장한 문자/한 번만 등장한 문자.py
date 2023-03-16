def solution(s):
    if len(s) == 1: return s
    answer = ""
    s = sorted(list(s))
    i = 0
    while i < len(s):
        if i != len(s) - 1 and s[i] == s[i + 1]:
            while i != len(s) - 1 and s[i] == s[i + 1]:
                i += 1
        else:
            answer += s[i]
        i += 1
    return answer
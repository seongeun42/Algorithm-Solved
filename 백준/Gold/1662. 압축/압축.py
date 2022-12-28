def decode(idx):
    ans = 0
    while idx < len(s):
        if s[idx].isdecimal():
            ans += 1
            idx += 1
        elif s[idx] == '(':
            nextIdx, n = decode(idx + 1)
            ans += int(s[idx - 1]) * n - 1
            idx = nextIdx
        elif s[idx] == ')':
            return [idx + 1, ans]
    return [idx + 1, ans]

s = input()
print(decode(0)[1])
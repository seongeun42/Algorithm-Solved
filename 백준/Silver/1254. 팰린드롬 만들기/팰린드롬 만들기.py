s = input()
res = len(s) * 2 - 1
for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        res = len(s) + i
        break
print(res)
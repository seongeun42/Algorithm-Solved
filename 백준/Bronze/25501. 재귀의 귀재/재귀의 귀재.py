def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l + 1, r - 1)

t = int(input())
for _ in range(t):
    s = input()
    cnt = 0
    isR = recursion(s, 0, len(s) - 1)
    print(isR, cnt)
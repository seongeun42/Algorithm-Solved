import sys
input = sys.stdin.readline
n = int(input())
k = [int(input()) for _ in range(n)]
s = []
res = 0
while k:
    v = k.pop()
    while s and v > s[-1][0]:
        res += s.pop()[1]
    if s and v == s[-1][0]:
        res += s[-1][1] if len(s) == 1 else s[-1][1] + 1
        s[-1][1] += 1
    else:
        if s: res += 1
        s.append([v, 1])
print(res)
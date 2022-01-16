import sys
input = sys.stdin.readline
n = int(input())
s, cnt = [], 0
for _ in range(n):
    v = int(input())
    while s and s[-1] <= v:
        s.pop()
    cnt += len(s)
    s.append(v)
print(cnt)
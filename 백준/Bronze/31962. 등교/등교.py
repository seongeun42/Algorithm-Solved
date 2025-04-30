import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = sorted([[*map(int, input().split())] for _ in range(n)], key=lambda x: (-x[0], x[1]))
for s, t in arr:
    if s + t <= x:
        print(s)
        break
else:
    print(-1)
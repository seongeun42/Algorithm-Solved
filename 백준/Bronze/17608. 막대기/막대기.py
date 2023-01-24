import sys
input = sys.stdin.readline

n = int(input())
h = [int(input()) for _ in range(n)]
mh = h[-1]
ans = 1
for i in range(n - 2, -1, -1):
    if h[i] > mh:
        ans += 1
        mh = h[i]
print(ans)
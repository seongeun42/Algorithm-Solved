import sys
input = sys.stdin.readline

N = int(input())
top = [*map(int, input().split())]
ans = max(top[0], top[-1])
for i in range(1, N - 1):
    height = top[i] + min(top[i - 1], top[i + 1])
    if ans < height:
        ans = height
print(ans)
import sys, math
input = sys.stdin.readline

N = int(input())
v = [*map(int, input().split())]
ans = v[-1]
for i in range(N - 2, -1, -1):
    if v[i] > ans:
        ans = v[i]
    elif ans % v[i] != 0:
        ans = v[i] * int(math.ceil(ans / v[i]))
print(ans)
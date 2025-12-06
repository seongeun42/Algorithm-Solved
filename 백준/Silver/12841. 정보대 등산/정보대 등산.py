import sys
input = sys.stdin.readline

n = int(input())
cross = [*map(int, input().split())]
left = [0] + [*map(int, input().split())]
right = [0] + [*map(int, input().split())]
for i in range(1, n):
    left[i] += left[i - 1]
    right[i] += right[i - 1]
ans = [-1, 1e12]
for i in range(n):
    dist = left[i] + cross[i] - right[i] + right[-1]
    if dist < ans[1]:
        ans = [i + 1, dist]
print(*ans)
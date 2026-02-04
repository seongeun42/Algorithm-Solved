import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
A = [*map(int, input().split())]
height = sorted([*map(int, input().split())])
width = set()
for i in range(N):
    for j in range(i + 1, N):
        width.add(abs(A[j] - A[i]))
ans = 0
for w in width:
    s, e = 0, M - 1
    area = 0
    while s <= e:
        mid = (s + e) // 2
        v = w * height[mid]
        if v <= R * 2:
            s = mid + 1
            area = v
        else:
            e = mid - 1
    if ans < area:
        ans = area
print(f"{ans / 2:.1f}" if ans > 0 else -1)
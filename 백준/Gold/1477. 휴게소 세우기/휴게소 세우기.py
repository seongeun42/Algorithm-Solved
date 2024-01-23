import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
locations = sorted([0] + [*map(int, input().split())] + [L])
s, e = 1, L - 1
ans = 0
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for i in range(1, len(locations)):
        dist = locations[i] - locations[i - 1]
        if dist > mid:
            cnt += (dist - 1) // mid
    if cnt > M:
        s = mid + 1
    else:
        e = mid - 1
        ans = mid
print(ans)
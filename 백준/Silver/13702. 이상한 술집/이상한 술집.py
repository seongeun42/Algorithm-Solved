import sys
input = sys.stdin.readline

N, K = map(int, input().split())
vol = [int(input()) for _ in range(N)]
s, e = 1, max(vol)
ans = 0
while s <= e:
    mid = (s + e) // 2
    total = 0
    for v in vol:
        total += v // mid
    if total >= K:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1
print(ans)
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    S = sorted([*map(int, input().split())])
    start, end = 0, n - 1
    minimum = 2 * 1e9
    ans = 0
    while start < end:
        hap = S[start] + S[end]
        if abs(k - hap) < minimum:
            minimum = abs(k - hap)
            ans = 0
        if hap <= k:
            start += 1
        else:
            end -= 1
        if abs(k - hap) == minimum:
            ans += 1
    print(ans)
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
cnt = defaultdict(int)
for _ in range(N):
    s, e = map(int, input().split())
    cnt[s] += 1
    cnt[e] -= 1
cnt = sorted(list(cnt.items()))
ans = 0
tmp = 0
for v in cnt:
    tmp += v[1]
    ans = max(ans, tmp)
print(ans)
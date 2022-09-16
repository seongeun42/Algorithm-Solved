import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]
ans = 0
for v in T:
    if v in S:
        ans += 1
print(ans)
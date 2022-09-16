import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set(input() for _ in range(N))
ans = 0
for _ in range(M):
    if input() in S:
        ans += 1
print(ans)
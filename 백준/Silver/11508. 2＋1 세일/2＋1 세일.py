import sys
input = sys.stdin.readline

N = int(input())
C = sorted([int(input()) for _ in range(N)], reverse=True)
ans = 0
cnt = N // 3
for i in range(cnt):
    ans += C[i * 3] + C[i * 3 + 1]
if N % 3 > 0:
    mod = N % 3
    for i in range(mod):
        ans += C[N - i - 1]
print(ans)
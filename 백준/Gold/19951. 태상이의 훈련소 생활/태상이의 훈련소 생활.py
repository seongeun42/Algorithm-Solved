import sys
input = sys.stdin.readline

N, M = map(int, input().split())
H = [*map(int, input().split())]
amount = [0] * (N + 1)
for _ in range(M):
    a, b, k = map(int, input().split())
    amount[a - 1] += k
    amount[b] -= k
H[0] += amount[0]
for i in range(1, N):
    amount[i] += amount[i - 1]
    H[i] += amount[i]
print(*H)
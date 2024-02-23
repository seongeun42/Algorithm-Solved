import sys
input = sys.stdin.readline

M, N = map(int, input().split())
larva = [[1] * M for _ in range(M)]
first = [0] * (2 * M - 1)
for _ in range(N):
    zero, one, two = map(int, input().split())
    for i in range(one):
        first[zero + i] += 1
    for i in range(two):
        first[zero + one + i] += 2
for i in range(len(first)):
    y = 0 if i >= M else M - i - 1
    x = i - M + 1 if i >= M else 0
    larva[y][x] += first[i]
for i in range(1, M):
    for j in range(1, M):
        larva[i][j] = max(larva[i - 1][j], larva[i - 1][j - 1], larva[i][j - 1])
for i in range(M):
    print(*larva[i])
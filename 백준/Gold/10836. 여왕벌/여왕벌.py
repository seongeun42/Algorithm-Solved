import sys
input = sys.stdin.readline

M, N = map(int, input().split())
larva = [[1] * M for _ in range(M)]
grow = [[0] * M for _ in range(M)]
for _ in range(N):
    zero, one, two = map(int, input().split())
    idx = zero
    while one > 0 and 0 <= idx < M:
        larva[M - idx - 1][0] += 1
        grow[M - idx - 1][0] = 1
        one -= 1
        idx += 1
    while one > 0 and M <= idx < 2 * M:
        larva[0][idx - M + 1] += 1
        grow[0][idx - M + 1] = 1
        one -= 1
        idx += 1
    while one == 0 and two > 0 and 0 <= idx < M:
        larva[M - idx - 1][0] += 2
        grow[M - idx - 1][0] = 2
        two -= 1
        idx += 1
    while one == 0 and two > 0 and M <= idx < 2 * M:
        larva[0][idx - M + 1] += 2
        grow[0][idx - M + 1] = 2
        two -= 1
        idx += 1
    for i in range(1, M):
        for j in range(1, M):
            mg = max(grow[i - 1][j], grow[i - 1][j - 1], grow[i][j - 1])
            larva[i][j] += mg
            grow[i][j] = mg
for i in range(M):
    print(*larva[i])
import sys
input = sys.stdin.readline

ans = float("inf")

def backtrack(cur, visited, G, time, cnt):
    global ans
    if time > ans:
        return
    if cnt == len(visited):
        if time < ans:
            ans = time
        return
    for i in range(len(G)):
        if not visited[i]:
            visited[i] = True
            backtrack(i, visited, G, time + G[cur][i], cnt + 1)
            visited[i] = False

def solve():
    N, K = map(int, input().split())
    T = [[*map(int, input().split())] for _ in range(N)]
    for m in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if T[i][m] + T[m][j] < T[i][j]:
                    T[i][j] = T[i][m] + T[m][j]
    visited = [False] * N
    visited[K] = True
    backtrack(K, visited, T, 0, 1)
    print(ans)

solve()
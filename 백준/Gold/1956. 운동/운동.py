import sys
input = sys.stdin.readline

def solve():
    V, E = map(int, input().split())
    G = [[1e9] * V for _ in range(V)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        G[a - 1][b - 1] = c
    for m in range(V):
        for i in range(V):
            for j in range(V):
                if G[i][j] > G[i][m] + G[m][j]:
                    G[i][j] = G[i][m] + G[m][j]
    ans = 1e9
    for i in range(V):
        if ans > G[i][i]:
            ans = G[i][i]
    print(ans if ans != 1e9 else -1)
    
solve()
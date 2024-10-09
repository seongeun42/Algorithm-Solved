import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find_circle(G, visited, cur):
    v = 0
    for n in G[cur]:
        if n == visited[cur]:
            continue
        if not visited[n]:
            visited[n] = cur
            v = find_circle(G, visited, n)
            if v < 0:
                break
        else:
            v = -n
            break
    visited[cur] = v
    return v if v != -cur else 0

def solve():
    N = int(input())
    G = [[] for _ in range(N + 1)]
    for _ in range(N):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    visited = [0] * (N + 1)
    visited[1] = 1
    find_circle(G, visited, 1)
    D = [-1] * (N + 1)
    stack = []
    for i in range(1, N + 1):
        if visited[i] < 0:
            D[i] = 0
            stack.append(i)
    while stack:
        station = stack.pop()
        for nxt in G[station]:
            if D[nxt] == -1:
                D[nxt] = D[station] + 1
                stack.append(nxt)
    print(' '.join(map(str, D[1:])))

solve()
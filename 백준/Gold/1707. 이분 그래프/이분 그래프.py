from collections import deque
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(node, color):
    visited[node] = color
    for n in G[node]:
        if not visited[n]:
            if dfs(n, -color) == "NO":
                return "NO"
        elif visited[n] == color:
            return "NO"
    return "YES"

def bfs(start):
    q = deque([[start, 1]])
    visited[start] = 1
    while q:
        node, color = q.popleft()
        for n in G[node]:
            if not visited[n]:
                visited[n] = -color
                q.append([n, -color])
            elif visited[n] == color:
                return "NO"
    return "YES"

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        G[n1].append(n2)
        G[n2].append(n1)
    visited = [0] * (V + 1)
    ans = 1
    for i in range(1, V + 1):
        if not visited[i]:
            if dfs(i, 1) == "NO":
            # if bfs(i) == "NO":
                ans = 0
                break
    print("YES" if ans else "NO")
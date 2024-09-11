from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, G, visited):
    q = deque([start])
    visited[start] = 1
    while q:
        cur = q.popleft()
        for nxt in G[cur]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = -visited[cur]
            elif visited[nxt] == visited[cur]:
                return False
    return True

def solve():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        G = [[] for _ in range(n + 1)]
        for _ in range(m):
            x, y = map(int, input().split())
            G[x].append(y)
            G[y].append(x)
        visited = [0] * (n + 1)
        for i in range(1, n + 1):
            if not visited[i]:
                if bfs(i, G, visited) == False:
                    print("impossible")
                    break
        else:
            print("possible")

solve()
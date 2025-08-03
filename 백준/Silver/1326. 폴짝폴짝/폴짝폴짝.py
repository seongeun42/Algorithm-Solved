from collections import deque

def bfs(a, b, N, bridge):
    q = deque([a - 1])
    visited = [-1] * N
    visited[a - 1] = 0
    while q:
        cur = q.popleft()
        if cur == b - 1:
            return visited[cur]
        term = bridge[cur]
        for nxt in range(cur + term, N, term):
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)
        for nxt in range(cur - term, -1, -term):
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)
    return -1

def solve():
    N = int(input())
    bridge = [*map(int, input().split())]
    a, b = map(int, input().split())
    print(bfs(a, b, N, bridge))

solve()
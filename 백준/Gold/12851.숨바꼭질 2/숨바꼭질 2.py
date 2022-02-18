from collections import deque

def bfs():
    q = deque([N])
    visited[N][0] = 0
    visited[N][1] = 1
    while q:
        v = q.popleft()
        for i in [2 * v, v + 1, v - 1]:
            if 0 <= i <= 100000:
                if visited[i][0] == -1:
                    visited[i][0] = visited[v][0] + 1
                    visited[i][1] = visited[v][1]
                    q.append(i)
                elif visited[i][0] == visited[v][0] + 1:
                    visited[i][1] += visited[v][1]

N, K = map(int, input().split())
visited = [[-1, 0] for _ in range(100001)]
bfs()
print(*visited[K], sep='\n')
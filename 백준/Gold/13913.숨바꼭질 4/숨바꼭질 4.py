from collections import deque

def bfs():
    q = deque([[N, [N]]])
    visited[N] = 1
    while q:
        v, arr = q.popleft()
        if v == K:
            print(len(arr) - 1)
            print(*arr, sep=' ')
            return
        if v * 2 <= 100000 and not visited[v * 2]:
            visited[v * 2] = 1
            q.append([v * 2, arr + [v * 2]])
        if v - 1 >= 0 and not visited[v - 1]:
            visited[v - 1] = 1
            q.append([v - 1, arr + [v - 1]])
        if v + 1 <= 100000 and not visited[v + 1]:
            visited[v + 1] = 1
            q.append([v + 1, arr + [v + 1]])

N, K = map(int, input().split())
if K < N:
    print(N - K)
    print(*range(N, K-1, -1), sep=' ')
else:
    visited = [0] * 100001
    bfs()
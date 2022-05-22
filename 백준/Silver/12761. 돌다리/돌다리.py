from collections import deque

def bfs(s):
    q = deque([s])
    visit[s] = 1
    while q:
        cur = q.popleft()
        if cur == M:
            return visit[M] - 1
        for i, m in enumerate(move):
            next = cur + m if i < 6 else cur * m
            if 0 <= next <= 100000 and not visit[next]:
                visit[next] = visit[cur] + 1
                q.append(next)

A, B, N, M = map(int, input().split())
move = [1, -1, A, B, -A, -B, A, B]
visit = [0] * 100001
print(bfs(N))
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
M = [list(input().rstrip()) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = set([(0, 0, M[0][0])])
    cnt = 1
    while q:
        x, y, path = q.pop()
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if 0 <= a < C and 0 <= b < R and M[b][a] not in path:
                q.add((a, b, path + M[b][a]))
                cnt = max(cnt, len(path) + 1)
    return cnt

print(bfs())
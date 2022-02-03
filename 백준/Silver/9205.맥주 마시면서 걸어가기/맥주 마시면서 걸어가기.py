from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque([[home[0], home[1]]])
    visited = [0] * n
    while q:
        x, y = q.popleft()
        if abs(x - fest[0]) + abs(y - fest[1]) <= 1000:
            print("happy")
            return
        for i, v in enumerate(conv):
            if not visited[i] and abs(x - v[0]) + abs(y - v[1]) <= 1000:
                q.append(v)
                visited[i] = 1
    print("sad")

t = int(input())
for _ in range(t):
    n = int(input())
    home = [*map(int, input().split())]
    conv = [[*map(int, input().split())] for _ in range(n)]
    fest = [*map(int, input().split())]
    bfs()
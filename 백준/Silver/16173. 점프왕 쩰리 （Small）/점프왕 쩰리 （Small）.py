from collections import deque
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    board = [[*map(int, input().split())] for _ in range(N)]
    direction = [(0, 1), (1, 0)]
    q = deque([(0, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True
    ans = "Hing"
    while q:
        cy, cx = q.popleft()
        if board[cy][cx] == -1:
            ans = "HaruHaru"
            break
        for dy, dx in direction:
            ny, nx = cy + (dy * board[cy][cx]), cx + (dx * board[cy][cx])
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))
    print(ans)

solve()
from collections import deque

n = int(input())
arr = [[0] * n for _ in range(n)]

max_height = 0
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        max_height = max(max_height, data[j])
        arr[i][j] = data[j]


def bfs(i: int, j: int, arr: list[list[int]], visited: list[list[bool]], height: int):
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    visited[i][j] = True
    queue = deque()
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            adj_x = x + dx[k]
            adj_y = y + dy[k]

            if adj_x < 0 or adj_x >= n or adj_y < 0 or adj_y >= n:
                continue

            if not visited[adj_x][adj_y] and arr[adj_x][adj_y] > height:
                visited[adj_x][adj_y] = True
                queue.append((adj_x, adj_y))


answer = 0

for height in range(0,101):
    count = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > height:
                count += 1
                bfs(i, j, arr, visited, height)

    answer = max(answer, count)

print(answer)

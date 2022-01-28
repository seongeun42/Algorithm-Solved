n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
for m in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] or (graph[i][m] and graph[m][j]):
                graph[i][j] = 1
for v in graph:
    print(*v, sep=' ')
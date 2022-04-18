N, D = map(int, input().split())
short = [[*map(int, input().split())] for _ in range(N)]
dist = [i for i in range(D + 1)]
for i in range(D + 1):
    if i > 0:
        dist[i] = min(dist[i], dist[i - 1] + 1)
    for s, e, v in short:
        if s == i and e <= D:
            dist[e] = min(dist[e], dist[s] + v)
print(dist[D])
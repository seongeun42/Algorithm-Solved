def dragonCurve(x, y, d, g):
    curve = [(x, y), (x + dx[d], y + dy[d])]
    for _ in range(g):
        cnt = len(curve)
        for i in range(cnt - 2, -1, -1):
            pre, cur = curve[i + 1], curve[i]
            move = movePoint[(pre[0] - cur[0], pre[1] - cur[1])]
            nextD = (curve[-1][0] + move[0], curve[-1][1] + move[1])
            curve.append(nextD)
    return set(curve)

pan = [[0] * 101 for _ in range(101)]
movePoint = {(1, 0): [0, -1],
        (0, 1): [1, 0],
        (-1, 0): [0, 1],
        (0, -1): [-1, 0]}
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())
    curve = dragonCurve(x, y, d, g)
    for cx, cy in curve:
        if 0 <= cx <= 100 and 0 <= cy <= 100:
            pan[cy][cx] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if pan[i][j] and pan[i + 1][j] and pan[i][j + 1] and pan[i + 1][j + 1]:
            ans += 1

print(ans)
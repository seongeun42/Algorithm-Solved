import sys
input = sys.stdin.readline

T = int(input())
D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for _ in range(T):
    x, y, direction = 0, 0, 0
    x1, y1, x2, y2 = 0, 0, 0, 0
    cmd = input().strip()
    for v in cmd:
        if v == 'F':
            x += D[direction][0]
            y += D[direction][1]
        elif v == 'B':
            x += D[(direction + 2) % 4][0]
            y += D[(direction + 2) % 4][1]
        elif v == 'L':
            direction = (direction + 3) % 4
        elif v == 'R':
            direction = (direction + 1) % 4
        x1, x2 = min(x1, x), max(x2, x)
        y1, y2 = max(y1, y), min(y2, y)
    print((x2 - x1) * (y1 - y2))
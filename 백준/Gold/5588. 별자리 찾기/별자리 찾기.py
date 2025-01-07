import sys
input = sys.stdin.readline

def solve():
    m = int(input())
    target = [[*map(int, input().split())] for _ in range(m)]
    n = int(input())
    star = {tuple([*map(int, input().split())]) for _ in range(n)}
    for sx, sy in star:
        x_diff, y_diff = sx - target[0][0], sy - target[0][1]
        for tx, ty in target:
            nx, ny = tx + x_diff, ty + y_diff
            if (nx, ny) not in star:
                break
        else:
            print(x_diff, y_diff)
            return

solve()
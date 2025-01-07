import sys
input = sys.stdin.readline

def solve():
    m = int(input())
    target = {tuple([*map(int, input().split())]) for _ in range(m)}
    n = int(input())
    star = {tuple([*map(int, input().split())]) for _ in range(n)}
    target_tmp = target.pop()
    target.add(target_tmp)
    for sx, sy in star:
        x_diff, y_diff = sx - target_tmp[0], sy - target_tmp[1]
        for tx, ty in target:
            nx, ny = tx + x_diff, ty + y_diff
            if (nx, ny) not in star:
                break
        else:
            print(x_diff, y_diff)
            return

solve()
import sys
input = sys.stdin.readline

def recursive(y, x, paper, n, cnt):
    pre, isEqual = paper[y][x], True
    for i in range(y, y + n):
        for j in range(x, x + n):
            if pre != paper[i][j]:
                isEqual = False
                break
        if not isEqual: break
    if isEqual:
        if pre == -1: cnt[0] += 1
        elif pre == 0: cnt[1] += 1
        elif pre == 1: cnt[2] += 1
    else:
        v = n // 3
        for k in range(3):
            for r in range(3):
                recursive(k * v + y, r * v + x, paper, v, cnt)

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
cnt = [0, 0, 0]
recursive(0, 0, paper, n, cnt)
print(*cnt, sep="\n")
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    X = [*map(int, input().split())]
    exist = [0] * 1000001
    maxX = 0
    for x in X:
        exist[x] = 1
        if maxX < x:
            maxX = x
    score = [0] * (maxX + 1)
    for x in X:
        for v in range(x + x, maxX + 1, x):
            if exist[v]:
                score[v] -= 1
                score[x] += 1
    for x in X:
        print(score[x], end=" ")

solve()
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    homework = sorted([[*map(int, input().split())] for _ in range(N)], key=lambda x: -x[1])
    days = [True] * 1001
    scores = 0
    for d, w in homework:
        while not days[d]:
            d -= 1
        if d != 0:
            days[d] = False
            scores += w
    print(scores)

solve()
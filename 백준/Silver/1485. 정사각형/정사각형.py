import sys
input = sys.stdin.readline

def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def solve():
    T = int(input())
    for _ in range(T):
        p = sorted([[*map(int, input().split())] for _ in range(4)])
        if dist(p[0], p[1]) == dist(p[0], p[2]) == dist(p[3], p[1]) == dist(p[3], p[2]):
            if dist(p[0], p[3]) == dist(p[1], p[2]):
                print(1)
                continue
        print(0)

solve()
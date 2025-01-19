import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    cow = sorted([[*map(int, input().split())] for _ in range(N)], key=lambda x: x[0])
    time = 0
    for s, t in cow:
        time = max(s, time) + t
    print(time)

solve()
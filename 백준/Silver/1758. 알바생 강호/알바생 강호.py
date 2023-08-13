import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    tips = sorted([int(input()) for _ in range(N)], reverse=True)
    print(sum([tips[i] - i for i in range(N) if tips[i] - i > 0]))

solve()
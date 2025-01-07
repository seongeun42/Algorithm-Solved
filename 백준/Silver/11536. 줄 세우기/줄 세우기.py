import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    names = [input().rstrip() for _ in range(N)]
    if names == sorted(names):
        print("INCREASING")
    elif names == sorted(names, reverse=True):
        print("DECREASING")
    else:
        print("NEITHER")

solve()
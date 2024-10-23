import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    M = int(input())
    print(sum([A[int(input()) - 1] for _ in range(M)]))

solve()
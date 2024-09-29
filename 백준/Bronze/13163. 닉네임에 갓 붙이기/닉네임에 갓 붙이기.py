import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    for _ in range(N):
        nick = input().rstrip().split()
        nick[0] = "god"
        print("".join(nick))

solve()
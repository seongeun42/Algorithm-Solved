import sys
input = sys.stdin.readline

def recursion(chairs, r, c, n):
    if n == 1:
        return chairs[r][c]
    else:
        nxt = n // 2
        pick = [recursion(chairs, r, c, nxt),
                recursion(chairs, r + nxt, c, nxt),
                recursion(chairs, r, c + nxt, nxt),
                recursion(chairs, r + nxt, c + nxt, nxt)]
        return sorted(pick)[1]

def solve():
    N = int(input())
    chairs = [[*map(int, input().split())] for _ in range(N)]
    print(recursion(chairs, 0, 0, N))

solve()
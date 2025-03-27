import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    boss = [0] + [*map(int, input().split())]
    praise = [0] * (n + 1)
    for _ in range(m):
        i, w = map(int, input().split())
        praise[i] += w
    for i in range(2, n + 1):
        praise[i] += praise[boss[i]]
    print(*praise[1:])

solve()
import sys
input = sys.stdin.readline

def solve():
    N, K, Q, M = map(int, input().split())
    sleep = set([*map(int, input().split())])
    code = [*map(int, input().split())]
    prefix = [1] * (N + 3)
    for c in code:
        if c in sleep:
            continue
        for v in range(c, N + 3, c):
            if v not in sleep:
                prefix[v] = 0
    for i in range(3, N + 3):
        prefix[i] += prefix[i - 1]
    for _ in range(M):
        S, E = map(int, input().split())
        print(prefix[E] - prefix[S - 1])

solve()
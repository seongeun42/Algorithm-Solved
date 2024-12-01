from collections import deque

def bfs(total, A, C):
    q = deque([(A, C)])
    visited = [[False] * (total + 1) for _ in range(total + 1)]
    visited[A][C] = True
    while q:
        a, c = q.popleft()
        b = total - a - c
        if a == b == c:
            return 1
        for small, big in {(a, b), (b, c), (a, c)}:
            if small == big:
                continue
            if small > big:
                small, big = big, small
            small, big = small * 2, big - small
            min_v = min(small, big, total - small - big)
            max_v = max(small, big, total - small - big)
            if not visited[min_v][max_v]:
                visited[min_v][max_v] = True
                q.append((min_v, max_v))
    return 0

def solve():
    A, B, C = sorted([*map(int, input().split())])
    if (A + B + C) % 3 != 0:
        print(0)
        return
    print(bfs(A + B + C, A, C))

solve()
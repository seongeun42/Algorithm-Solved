import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    n = int(input())
    arr = [[*map(int, input().split())] for _ in range(n)]
    R = list(range(n))
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                ir = find_root(i, R)
                jr = find_root(j, R)
                if ir != jr:
                    R[max(ir, jr)] = min(ir, jr)
    group = {}
    for i, v in enumerate(R):
        if i == v:
            group[i + 1] = [i + 1]
        else:
            group[find_root(i, R) + 1].append(i + 1)
    for g in group.values():
        size = len(g)
        if size == 1:
            print(0)
            return
        for i in range(size):
            for j in range(i, size):
                a, b = g[i] - 1, g[j] - 1
                if arr[a][b] == 1:
                    print(0)
                    return
    print(len(group))
    for arr in group.values():
        print(*arr)

solve()
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_root(node):
    if R[node] != node:
        R[node] = find_root(R[node])
    return R[node]

while 1:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    R = [i for i in range(m)]
    E = sorted([[*map(int, input().split())] for _ in range(n)], key=lambda x: x[2])
    res = 0
    for x, y, z in E:
        xr = find_root(x)
        yr = find_root(y)
        if xr != yr:
            res += z
            R[max(xr, yr)] = min(xr, yr)
    print(sum([e[2] for e in E]) - res)
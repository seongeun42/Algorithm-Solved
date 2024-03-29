import sys
input = sys.stdin.readline

def find_root(node):
    if R[node] != node:
        R[node] = find_root(R[node])
    return R[node]

def union(n1, n2):
    n1 = find_root(n1)
    n2 = find_root(n2)

    if n1 < n2:
        R[n2] = n1
    elif n1 > n2:
        R[n1] = n2

n, m = map(int, input().split())
E = sorted([[*map(int, input().split())] for _ in range(m)], key=lambda x: x[2])
R = [i for i in range(n + 1)]
maxC = -1
res = 0
for a, b, c in E:
    if find_root(a) != find_root(b):
        res += c
        maxC = max(maxC, c)
        union(a, b)
print(res - maxC)
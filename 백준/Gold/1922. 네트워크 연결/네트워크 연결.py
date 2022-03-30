import sys
input = sys.stdin.readline

def find_root(node):
    if R[node] != node:
        return find_root(R[node])
    return node

def union(n1, n2):
    n1 = find_root(n1)
    n2 = find_root(n2)
    R[n1] = n2

N = int(input())
M = int(input())
R = [i for i in range(N + 1)]
E = sorted([[*map(int, input().split())] for _ in range(M)], key=lambda x: x[2])
res = 0
for a, b, c in E:
    if find_root(a) != find_root(b):
        res += c
        union(a, b)
print(res)
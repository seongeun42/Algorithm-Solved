import sys
input = sys.stdin.readline

def find_root(node):
    if R[node] != node:
        R[node] = find_root(R[node])
    return R[node]

n = int(input())
R = [i for i in range(n)]
E = []
for i in range(n):
    c = [*map(int, input().split())]
    for j in range(i + 1, n):
        E.append((c[j], i, j))
E.sort()

res = 0
for c, i, j in E:
    ir = find_root(i)
    jr = find_root(j)
    if ir != jr:
        res += c
        R[max(ir, jr)] = min(ir, jr)
print(res)
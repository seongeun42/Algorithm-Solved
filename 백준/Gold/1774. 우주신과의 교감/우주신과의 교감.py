import sys
input = sys.stdin.readline

def find_root(node):
    if R[node] != node:
        R[node] = find_root(R[node])
    return R[node]

def calDist(n1, n2):
    x1, y1 = node[n1]
    x2, y2 = node[n2]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

n, m = map(int, input().split())
node = {(i + 1): tuple(map(int, input().split())) for i in range(n)}
edge = []
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        edge.append((calDist(i, j), i, j))
for i in range(m):
    a, b = map(int, input().split())
    edge.append((0, a, b))
edge.sort()

R = [i for i in range(n + 1)]

res = 0
for c, i, j in edge:
    ir = find_root(i)
    jr = find_root(j)
    if ir != jr:
        res += c
        R[max(ir, jr)] = R[min(ir, jr)]

print(f"{res:.2f}")
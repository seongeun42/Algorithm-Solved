import sys
input = sys.stdin.readline

def find_root(n):
    if R[n] != n:
        R[n] = find_root(R[n])
    return R[n]

n, m = map(int, input().split())
R = [i for i in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    xr = find_root(x)
    yr = find_root(y)
    if xr != yr:
        R[max(xr, yr)] = min(xr, yr)

input()
E = []
for i in range(1, n):
    line = [*map(int, input().split())]
    for j in range(i + 1, n):
        E.append((line[j], j + 1, i + 1))
E.sort()

cost = 0
connect = []
for c, x, y in E:
    xr = find_root(x)
    yr = find_root(y)
    if xr != yr:
        cost += c
        connect.append((x, y))
        R[max(xr, yr)] = min(xr, yr)

print(cost, len(connect))
for x, y in connect:
    print(x, y)
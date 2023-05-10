import sys
input = sys.stdin.readline

def find_root(node):
    if R[node] != node:
        R[node] = find_root(R[node])
    return R[node]

n, m = map(int, input().split())
mw = ["-"] + list(input().split())
E = sorted([[*map(int, input().split())] for _ in range(m)], key=lambda x: x[2])
R = [i for i in range(n + 1)]
ans = 0
for u, v, d in E:
    if mw[u] != mw[v]:
        ur = find_root(u)
        vr = find_root(v)
        if ur != vr:
            ans += d
            if ur < vr:
                R[vr] = ur
            elif ur > vr:
                R[ur] = vr

for i in range(1, n + 1):
    find_root(i)

print(ans if len(set(R[1:])) == 1 else -1)
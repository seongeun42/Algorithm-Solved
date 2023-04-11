import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def find_root(node):
    if root[node] != node:
        root[node] = find_root(root[node])
    return root[node]

def union(n1, n2):
    n1 = find_root(n1)
    n2 = find_root(n2)

    if n1 < n2:
        root[n2] = n1
    elif n1 > n2:
        root[n1] = n2

n, m = map(int, input().split())
root = [i for i in range(n + 1)]
for _ in range(m):
    cmd, n1, n2 = map(int, input().split())
    if cmd == 0:
        union(n1, n2)
    else:
        print("YES" if find_root(n1) == find_root(n2) else "NO")
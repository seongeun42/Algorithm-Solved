import sys
input = sys.stdin.readline

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
know = [*map(int, input().split())]
party = [[*map(int, input().split())] for _ in range(m)]
root = [i for i in range(n + 1)]
G = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    n1 = party[i][1]
    for j in range(2, party[i][0] + 1):
        union(n1, party[i][j])

for i in range(1, n + 1):
    find_root(i)

knowRoot = set()
for v in know[1:]:
    knowRoot.add(root[v])

ans = 0
for i in range(m):
    ans += 1
    for v in party[i][1:]:
        if root[v] in knowRoot:
            ans -= 1
            break
print(ans)
import sys
input = sys.stdin.readline

def find_root(node):
    if R[node] != node:
        R[node] = find_root(R[node])
    return R[node]

n, m = map(int, input().split())
connect = [tuple(map(int, input().split())) for _ in range(m)]
R = [i for i in range(n)]
for i in range(m):
    a, b = connect[i]
    ar = find_root(a)
    br = find_root(b)
    if ar == br:
        print(i + 1)
        sys.exit()
    if ar < br:
        R[br] = ar
    elif ar > br:
        R[ar] = br
print(0)
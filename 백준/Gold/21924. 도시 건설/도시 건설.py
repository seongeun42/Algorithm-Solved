import sys
input = sys.stdin.readline

def find_root(n):
    if R[n] != n:
        R[n] = find_root(R[n])
    return R[n]

N, M = map(int, input().split())
E = sorted([[*map(int, input().split())] for _ in range(M)], key=lambda x: x[2])
R = [i for i in range(N + 1)]
total = 0
cost = 0
for a, b, c in E:
    total += c
    ar = find_root(a)
    br = find_root(b)
    if ar != br:
        cost += c
        if ar < br:
            R[br] = ar
        else:
            R[ar] = br

for i in range(1, N + 1):
    find_root(i)

if len(set(R)) != 2:
    print(-1)
else:
    print(total - cost)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_root(node):
    if R[node] != node:
        R[node] = find_root(R[node])
    return R[node]

T = int(input())
for tc in range(T):
    print(f"Scenario {tc + 1}:")
    n = int(input())
    k = int(input())
    R = [i for i in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        ar = find_root(a)
        br = find_root(b)
        R[max(ar, br)] = min(ar, br)

    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())
        print(0 if find_root(u) != find_root(v) else 1)
    if tc != T - 1:
        print()
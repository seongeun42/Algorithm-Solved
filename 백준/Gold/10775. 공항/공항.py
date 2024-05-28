import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    G = int(input())
    P = int(input())
    R = [i for i in range(G + 1)]
    gs = [int(input()) for _ in range(P)]
    ans = 0
    for v in gs:
        root = find_root(v, R)
        if root == 0:
            break
        ans += 1
        R[root] = find_root(root - 1, R)
    print(ans)

solve()
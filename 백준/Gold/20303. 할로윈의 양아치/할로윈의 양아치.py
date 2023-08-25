import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find_root(node, R):
    if R[node] < 0:
        return node
    else:
        R[node] = find_root(R[node], R)
    return R[node]

def solve():
    N, M, K = map(int, input().split())
    candy = [*map(int, input().split())]
    R = [-1] * (N + 1)
    W = [0] + [candy[i] for i in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        ar = find_root(a, R)
        br = find_root(b, R)
        if ar != br:
            if R[ar] <= R[br]:
                W[ar] += W[br]
                R[ar] += R[br]
                R[br] = ar
            else:
                W[br] += W[ar]
                R[br] += R[ar]
                R[ar] = br
    roots = []
    for i in range(1, N + 1):
        if R[i] < 0:
            roots.append(i)
    children = []
    for v in roots:
        if v == 0:
            continue
        children.append((W[v], -1 * R[v]))
    dp = [0] * K
    for cw, cc in children:
        for k in range(K - 1, cc - 1, -1):
            if dp[k] < cw + dp[k - cc]:
                dp[k] = cw + dp[k - cc]
    print(dp[K - 1])

solve()
import sys
input = sys.stdin.readline

high, far = 0, 0

def dfs(n, G, visit, total):
    visit[n] = 1
    global high, far
    if total > high:
        high = total
        far = n
    for nn, w in G[n]:
        if not visit[nn]:
            dfs(nn, G, visit, total + w)

def find_root(n, R):
    if R[n] < 0:
        return n
    R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, K = map(int, input().split())
    E = sorted([[*map(int, input().split())] for _ in range(K)], key=lambda x: x[2])
    G = [[] for _ in range(N)]
    R = [-1] * N
    # 최단 경로 찾기
    cnt, cost = 1, 0
    for a, b, c in E:
        ar = find_root(a, R)
        br = find_root(b, R)
        if ar != br:
            cost += c
            R[max(ar, br)] = min(ar, br)
            cnt += 1
            G[a].append((b, c))
            G[b].append((a, c))
        if cnt == N:
            break
    # 최단 경로 내에서 두 마을 간 가장 큰 비용 찾기
    visit = [0] * N
    dfs(0, G, visit, 0)
    visit = [0] * N
    dfs(far, G, visit, 0)
    print(cost, high, sep="\n")

solve()
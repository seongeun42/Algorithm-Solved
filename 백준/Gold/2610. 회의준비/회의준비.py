import sys
input = sys.stdin.readline

def floyd(committee, G):
    size = len(committee)
    if size == 1:
        return committee[0]
    idx = {committee[i]: i for i in range(size)}
    # 인접행렬 만들기
    arr = [[1e9] * size for _ in range(size)]
    for i in range(size):
        for v in G[committee[i]]:
            arr[i][idx[v]] = 1
    
    # 플로이드-워셜 수행
    for m in range(size):
        for i in range(size):
            for j in range(size):
                if i != j and arr[i][j] > arr[i][m] + arr[m][j]:
                    arr[i][j] = arr[i][m] + arr[m][j]
    
    # 대표 구하기
    rep, cost = 0, 1e9
    for i in range(size):
        c = max([v for v in arr[i] if v != 1e9])
        if cost > c:
            rep = committee[i]
            cost = c
    return rep

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N = int(input())
    
    # 위원회 나누기
    M = int(input())
    R = [i for i in range(N + 1)]
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        aRoot = find_root(a, R)
        bRoot = find_root(b, R)
        if aRoot != bRoot:
            R[min(aRoot, bRoot)] = max(aRoot, bRoot)
        G[a].append(b)
        G[b].append(a)
    committees = {}
    for i in range(1, N + 1):
        root = find_root(i, R)
        if root in committees:
            committees[root].append(i)
        else:
            committees[root] = [i]
    
    # 대표 뽑기
    representative = []
    for committee in committees.values():
        representative.append(floyd(committee, G))
    
    print(len(committees))
    print(*sorted(representative), sep="\n")
    
solve()
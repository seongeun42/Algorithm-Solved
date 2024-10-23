import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] < 0:
        return n
    R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N = int(input())
    E = [[*map(int, input().split())] for _ in range(N - 1)]
    C = "." + input().strip()
    R = [-1] * (N + 1)
    RB = []
    for u, v in E:
        if (C[u], C[v]) == ('B', 'B'):
            continue
        # 검정-빨강 연결 간선은 따로 기록
        if (C[u], C[v]) in {('R', 'B'), ('B', 'R')}:
            RB.append((u, v))
        else:
            # 빨강-빨강이면 연결
            ur = find_root(u, R)
            vr = find_root(v, R)
            if ur < vr:
                R[ur] += R[vr]
                R[vr] = ur
            elif ur > vr:
                R[vr] += R[ur]
                R[ur] = vr
    # 검정-빨강을 확인하며 빨강 개수만큼 더하기
    ans = 0
    for u, v in RB:
        ans += -R[find_root(v, R)] if C[u] == 'B' else -R[find_root(u, R)]
    print(ans)

solve()
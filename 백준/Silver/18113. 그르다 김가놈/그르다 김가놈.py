import sys
input = sys.stdin.readline

def solve():
    N, K, M = map(int, input().split())
    gimbap = []
    s, e = 1, 0
    for _ in range(N):
        L = int(input())
        if L <= K:
            continue
        L -= K if L < 2 * K else 2 * K
        if e < L:
            e = L
        gimbap.append(L)
    P = -1
    while s <= e:
        mid = (s + e) // 2
        cnt = 0
        for l in gimbap:
            cnt += l // mid
            if cnt >= M:
                break
        if cnt >= M:
            P = mid
            s = mid + 1
        else:
            e = mid - 1
    print(P)

solve()
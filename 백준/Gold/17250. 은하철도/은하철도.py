import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    N, M = map(int, input().split())
    R = [i for i in range(N + 1)]
    cnt = [0] * (N + 1)
    for i in range(N):
        cnt[i + 1] = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        ar = find_root(a, R)
        br = find_root(b, R)
        if ar != br:
            R[max(ar, br)] = min(ar, br)
            cnt[min(ar, br)] += cnt[max(ar, br)]
        print(cnt[min(ar, br)])

solve()
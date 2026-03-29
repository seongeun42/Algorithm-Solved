import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    T = int(input())
    for i in range(T):
        N, M = map(int, input().split())
        E = sorted([[*map(int, input().split())] for _ in range(M)], key=lambda x: x[2])
        R = list(range(N + 1))
        cnt = 1
        dist = 0
        for a, b, d in E:
            ar = find_root(a, R)
            br = find_root(b, R)
            if ar != br:
                cnt += 1
                dist += d
                R[max(ar, br)] = min(ar, br)
        print(f"Case #{i + 1}: {dist} meters")

solve()
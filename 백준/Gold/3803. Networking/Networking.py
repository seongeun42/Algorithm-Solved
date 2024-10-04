import sys
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    while 1:
        S = input()
        if S[0] == '0':
            return
        P, R = map(int, S.split())
        root = [i for i in range(P + 1)]
        E = sorted([[*map(int, input().split())] for _ in range(R)], key=lambda x: x[2])
        cnt = P
        cost = 0
        for u, v, w in E:
            ur = find_root(u, root)
            vr = find_root(v, root)
            if ur != vr:
                root[max(ur, vr)] = min(ur, vr)
                cnt -= 1
                cost += w
        print(cost)
        input()

solve()
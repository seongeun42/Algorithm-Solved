import sys, math
input = sys.stdin.readline

def move(fire, N):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    newFire = {}
    for k, v in fire.items():
        r, c = k
        for m, s, d in v:
            nr = r + dy[d] * s
            nc = c + dx[d] * s
            nr %= N
            nc %= N
            if (nr, nc) in newFire:
                newFire[(nr, nc)].append((m, s, d))
            else:
                newFire[(nr, nc)] = [(m, s, d)]
    return newFire

def change(fire):
    newFire = {}
    for k, v in fire.items():
        if len(v) == 1:
            newFire[k] = v
            continue
        nm, ns, nd = 0, 0, 0
        dFlag = v[0][2] % 2
        for m, s, d in v:
            nm += m
            ns += s
            if nd == 0 and dFlag != d % 2:
                nd = 1
        nm = math.floor(nm // 5)
        ns = math.floor(ns // len(v))
        if nm > 0:
            for i in range(0, 7, 2):
                if i > 0:
                    newFire[k].append((nm, ns, i + nd))
                else:
                    newFire[k] = [(nm, ns, i + nd)]
    return newFire

def solve():
    N, M, K = map(int, input().split())
    fire = {}
    for _ in range(M):
        r, c, m, s, d = map(int, input().split())
        if (r - 1, c - 1) in fire:
            fire[(r - 1, c - 1)].append((m, s, d))
        else:
            fire[(r - 1, c - 1)] = [(m, s, d)]
    for i in range(K):
        fire = change(move(fire, N))
    ans = 0
    for k, v in fire.items():
        for m, s, d in v:
            ans += m
    print(ans)

solve()
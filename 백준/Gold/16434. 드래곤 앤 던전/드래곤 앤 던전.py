import sys, math
input = sys.stdin.readline

def solve():
    N, atk = map(int, input().split())
    room = [[*map(int, input().split())] for _ in range(N)]
    mHP = cHP = 0
    for t, a, h in room:
        if t == 1:
            damage = a * (int(math.ceil(h / atk)) - 1)
            cHP += damage
            if cHP > mHP:
                mHP = cHP
        else:
            cHP = max(cHP - h, 0)
            atk += a
    print(mHP + 1)

solve()
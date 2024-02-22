import sys, math
input = sys.stdin.readline

def simulate(room, mHP, cHP, atk):
    for t, a, h in room:
        if t == 1:
            cnt = int(math.ceil(h / atk))
            if cHP <= a * (cnt - 1):
                return False
            cHP -= a * (cnt - 1)
        else:
            cHP = min(cHP + h, mHP)
            atk += a
    return True

def solve():
    N, atk = map(int, input().split())
    room = [[*map(int, input().split())] for _ in range(N)]
    s, e = 1, int(9e18)
    ans = 0
    while s <= e:
        mHP = (s + e) // 2
        alive = simulate(room, mHP, mHP, atk)
        if not alive:
            s = mHP + 1
        else:
            ans = mHP
            e = mHP - 1
    print(ans)

solve()
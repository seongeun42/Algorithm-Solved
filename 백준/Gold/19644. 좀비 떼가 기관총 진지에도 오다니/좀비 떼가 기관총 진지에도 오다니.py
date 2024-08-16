from collections import deque
import sys
input = sys.stdin.readline

def solve():
    L = int(input())
    ml, mk = map(int, input().split())
    C = int(input())
    Z = deque([int(input()) for _ in range(L)])
    shot = [0] * (L + 1)
    damage = 0
    ans = "YES"
    idx = 0
    while Z:
        hp = Z.popleft()
        if idx >= ml and shot[idx - ml]:
            damage -= mk
        if damage + mk >= hp:
            damage += mk
            shot[idx] = 1
        elif C > 0:
            C -= 1
        else:
            ans = "NO"
            break
        idx += 1
    print(ans)

solve()
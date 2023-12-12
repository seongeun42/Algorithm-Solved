import sys
input = sys.stdin.readline

def solve():
    garo, sero = map(int, input().split())
    n = int(input())
    store = [[*map(int, input().split())] for _ in range(n)]
    dg = [*map(int, input().split())]
    ans = 0
    for i in range(n):
        d, dist = store[i]
        if d == 1:
            if dg[0] == 1:
                ans += abs(dist - dg[1])
            elif dg[0] == 2:
                ans += sero + min(dist + dg[1], 2 * garo - (dist + dg[1]))
            elif dg[0] == 3:
                ans += dist + dg[1]
            else:
                ans += (garo - dist) + dg[1]
        elif d == 2:
            if dg[0] == 1:
                ans += sero + min(dist + dg[1], 2 * garo - (dist + dg[1]))
            elif dg[0] == 2:
                ans += abs(dist - dg[1])
            elif dg[0] == 3:
                ans += dist + (sero - dg[1])
            else:
                ans += (garo - dist) + (sero - dg[1])
        elif d == 3:
            if dg[0] == 1:
                ans += dist + dg[1]
            elif dg[0] == 2:
                ans += (sero - dist) + dg[1]
            elif dg[0] == 3:
                ans += abs(dist - dg[1])
            else:
                ans += garo + min(dist + dg[1], 2 * sero - (dist + dg[1]))
        else:
            if dg[0] == 1:
                ans += dist + (garo - dg[1])
            elif dg[0] == 2:
                ans += (sero - dist) + (garo - dg[1])
            elif dg[0] == 3:
                ans += garo + min(dist + dg[1], 2 * sero - (dist + dg[1]))
            else:
                ans += abs(dist - dg[1])
    print(ans)

solve()
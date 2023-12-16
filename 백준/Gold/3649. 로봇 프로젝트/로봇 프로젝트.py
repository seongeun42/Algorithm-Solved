import sys
input = sys.stdin.readline

def solve():
    while True:
        try:
            x = int(input()) * 10000000
            n = int(input())
            lego = sorted([int(input()) for _ in range(n)])
            s, e = 0, n - 1
            ans = "danger"
            while s < e:
                if lego[s] + lego[e] == x:
                    ans = f"yes {lego[s]} {lego[e]}"
                    break
                if lego[s] + lego[e] > x:
                    e -= 1
                else:
                    s += 1
            print(ans)
        except Exception:
            break

solve()
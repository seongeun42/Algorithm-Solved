import sys
input = sys.stdin.readline

def solve(q):
    live = {int(input())}
    print(0)
    for _ in range(q - 1):
        x = int(input())
        p = x
        res = 0 if x not in live else x
        while p != 1:
            p //= 2
            if p in live:
                res = p
        if res == 0:
            live.add(x)
        print(res)

if __name__ == "__main__" :
    n, q = map(int, input().split())
    solve(q)
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    A, B = map(int, input().split())
    coords = set([tuple([*map(int, input().split())]) for _ in range(N)])
    cnt = 0
    for x, y in coords:
        if (x + A, y) in coords and (x, y + B) in coords and (x + A, y + B) in coords:
            cnt += 1
    print(cnt)

solve()
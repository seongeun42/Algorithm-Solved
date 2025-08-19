import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    hole = [*map(int, input().split())]
    maxv = 0
    for i, h in enumerate(hole):
        if maxv < h + i:
            maxv = h + i
        hole[i] = maxv
    Q = int(input())
    acorn = [*map(int, input().split())]
    ans = []
    for a in acorn:
        s, e = 0, N - 1
        idx = 0
        while s <= e:
            mid = (s + e) // 2
            if a <= hole[mid]:
                idx = mid
                e = mid - 1
            else:
                s = mid + 1
        ans.append(idx + 1)
    print(*ans)

solve()
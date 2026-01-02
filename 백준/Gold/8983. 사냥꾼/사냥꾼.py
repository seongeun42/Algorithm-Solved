import sys
input = sys.stdin.readline

def solve():
    M, N, L = map(int, input().split())
    loca = sorted([*map(int, input().split())])
    animals = [[*map(int, input().split())] for _ in range(N)]
    ans = 0
    for a, b in animals:
        s, e = 0, M - 1
        while s <= e:
            mid = (s + e) // 2
            if abs(loca[mid] - a) + b <= L:
                ans += 1
                break
            elif loca[mid] < a:
                s = mid + 1
            else:
                e = mid - 1
    print(ans)

solve()
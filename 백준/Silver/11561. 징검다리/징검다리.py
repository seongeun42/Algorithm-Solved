import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s, e = 1, n
    res = 0
    while s <= e:
        mid = (s + e) // 2
        if (mid + 1) * mid // 2 <= n:
            res = mid
            s = mid + 1
        else:
            e = mid - 1
    print(res)
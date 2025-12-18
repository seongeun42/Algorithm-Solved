import sys
input = sys.stdin.readline

def solve():
    N, K, D = map(int, input().split())
    rule = [[*map(int, input().split())] for _ in range(K)]
    s, e = 1, N
    ans = 0
    while s <= e:
        mid = (s + e) // 2
        cnt = 0
        for A, B, C in rule:
            if mid >= B:
                cnt += (B - A) // C + 1
            elif A <= mid < B:
                cnt += (mid - A) // C + 1
        if cnt < D:
            s = mid + 1
        else:
            e = mid - 1
            ans = mid
    print(ans)

solve()
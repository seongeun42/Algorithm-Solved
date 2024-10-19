def solve():
    N = int(input())
    A = sorted([*map(int, input().split())])
    ans = 200_000_001
    l, r = 0, len(A) - 1
    while l < r:
        if ans == 0:
            break
        blend = A[l] + A[r]
        if abs(blend) < abs(ans):
            ans = blend
        if abs(A[l]) < abs(A[r]):
            r -= 1
        else:
            l += 1
    print(ans)

solve()
def solve():
    N = int(input())
    arr = sorted([*map(int, input().split())])
    ans = 1
    for v in arr:
        if ans < v:
            return ans
        ans += v
    return ans

print(solve())
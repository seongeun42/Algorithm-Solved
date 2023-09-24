def solve():
    N = int(input())
    nums = sorted([*map(int, input().split())])
    q, r = divmod(N, 2)
    print(nums[q + r - 1])

solve()
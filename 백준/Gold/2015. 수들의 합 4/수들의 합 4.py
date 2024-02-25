def solve():
    N, K = map(int, input().split())
    A = [*map(int, input().split())]
    total = ans = 0
    nums = {0 : 1}
    for i in range(N):
        total += A[i]
        ans += nums.get(total - K, 0)
        nums[total] = nums.get(total, 0) + 1
    print(ans)

solve()
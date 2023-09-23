def solve():
    N, M = map(int, input().split())
    A = [*map(int, input().split())]
    remain = [0] * M
    sum = 0
    for i in range(N):
        sum += A[i]
        remain[sum % M] += 1
    ans = remain[0]
    for v in remain:
        ans += v * (v - 1) // 2
    print(ans)

solve()
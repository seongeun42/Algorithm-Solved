def solve():
    n = int(input())
    a = [*map(int, input().split())]
    dp = [0]
    for i in range(n):
        s, e = 0, len(dp) - 1
        while s <= e:
            m = (s + e) // 2
            if dp[m] < a[i]:
                s = m + 1
            else:
                e = m - 1
        if s >= len(dp):
            dp.append(a[i])
        else:
            dp[s] = a[i]
    print(len(dp) - 1)

solve()
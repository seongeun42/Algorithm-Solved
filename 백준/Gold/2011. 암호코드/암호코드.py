n = input()
if n[0] == "0":
    print(0)
else:
    n = "0" + n
    dp = [0] * len(n)
    dp[0] = dp[1] = 1
    for i in range(2, len(n)):
        one = int(n[i])
        two = int(n[i - 1] + n[i])
        if one > 0:
            dp[i] += dp[i - 1]
        if 10 <= two <= 26:
            dp[i] += dp[i - 2]
    print(dp[-1] % 1000000)
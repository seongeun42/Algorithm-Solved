N = int(input())
dp = [False, False, True, False, True]
while len(dp) <= N:
    cnt = len(dp)
    if False in {dp[cnt - 1], dp[cnt - 3], dp[cnt - 4]}:
        dp.append(True)
    else:
        dp.append(False)
print("SK" if dp[N] else "CY")
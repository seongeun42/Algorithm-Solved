s1 = input()
s2 = input()
len1, len2 = len(s1), len(s2)
dp = [0] * (len2 + 1)
ans = 0
for i in range(len1):
    for j in range(len2, 0, -1):
        dp[j] = dp[j - 1] + 1 if s1[i] == s2[j - 1] else 0
        if ans < dp[j]:
            ans = dp[j]
print(ans)
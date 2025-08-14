dna = input()
N = len(dna)
dp = [[0] * N for _ in range(N)]
for i in range(1, N): # 뒤
    for j in range(i - 1, -1, -1): # 앞
        if (dna[j] == 'a' and dna[i] == 't') or (dna[j] == 'g' and dna[i] == 'c'):
            dp[j][i] = dp[j + 1][i - 1] + 2
        for mid in range(j, i):
            if dp[j][i] < dp[j][mid] + dp[mid + 1][i]:
                dp[j][i] = dp[j][mid] + dp[mid + 1][i]
print(dp[0][-1])
def dfs(x, y, dna, dp):
    if x >= y:
        return 0
    if dp[x][y] != -1:
        return dp[x][y]
    if (dna[x] == 'a' and dna[y] == 't') or (dna[x] == 'g' and dna[y] == 'c'):
        dp[x][y] = dfs(x + 1, y - 1, dna, dp) + 2
    for mid in range(x, y):
        v = dfs(x, mid, dna, dp) + dfs(mid + 1, y, dna, dp)
        if dp[x][y] < v:
            dp[x][y] = v
    return dp[x][y]

def solve():
    dna = input()
    N = len(dna)
    dp = [[-1] * N for _ in range(N)]
    dfs(0, N - 1, dna, dp)
    print(dp[0][N - 1])

solve()
def cal(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2

def solv(m, init):
    dp = [[init] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j == 0:
                dp[i][j] = num[jido[i][j]]
            elif jido[i][j] in ['+', '-', '*']:
                if 0 < i and 0 < j:
                    dp[i][j] = m(dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = dp[i - 1][j] if 0 < i else dp[i][j - 1]
            elif jido[i][j] in num:
                if 0 < i and 0 < j:
                    dp[i][j] = m(cal(dp[i - 1][j], num[jido[i][j]], jido[i - 1][j]),
                                cal(dp[i][j - 1], num[jido[i][j]], jido[i][j - 1]))
                else:
                    dp[i][j] = cal(dp[i - 1][j], num[jido[i][j]], jido[i - 1][j]) if 0 < i else \
                        cal(dp[i][j - 1], num[jido[i][j]], jido[i][j - 1])
    return dp[N - 1][N - 1]

N = int(input())
jido = [list(input().split()) for _ in range(N)]
num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
print(solv(max, -10), solv(min, int(1e9)))
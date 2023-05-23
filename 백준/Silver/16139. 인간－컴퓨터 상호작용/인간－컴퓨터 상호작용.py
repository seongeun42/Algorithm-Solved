import sys
input = sys.stdin.readline

s = input().rstrip()
q = int(input())
dp = [[0] * 26 for _ in range(len(s))]
a = ord('a')
dp[0][ord(s[0]) - a] = 1
for i in range(1, len(s)):
    for j in range(26):
        dp[i][j] = dp[i - 1][j]
    dp[i][ord(s[i]) - a] += 1
for _ in range(q):
    c, l, r = input().split()
    l, r = int(l), int(r)
    cnt = dp[r][ord(c) - a]
    if l != 0:
        cnt -= dp[l - 1][ord(c) - a]
    print(cnt)
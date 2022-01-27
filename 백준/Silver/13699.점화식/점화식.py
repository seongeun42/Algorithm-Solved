dp=[0]*36
dp[0]=1

N= int(input())

for i in range(1,N+1):
    for j in range(i):
        dp[i]+=dp[j]*dp[i-j-1]
print(dp[N])
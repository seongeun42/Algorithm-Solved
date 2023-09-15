import sys
input = sys.stdin.readline

if __name__ == "__main__":
    dp = [0] + [1] * 1000000
    hap = [0] * 1000001
    hap[1] = 1
    for i in range(2, 1000001):
        for j in range(i, 1000001, i):
            dp[j] += i
        hap[i] = hap[i - 1] + dp[i]
    
    T = int(input())
    ans = []
    for _ in range(T):
        n = int(input())
        ans.append(hap[n])
    print(*ans, sep='\n')
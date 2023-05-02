import sys
input = sys.stdin.readline

def dfs(num, dep):
    if dep == k:
        return
    for i in range(n):
        nextNum = num + nums[i]
        make.add(nextNum)
        if dp[dep + 1][nextNum] != 1:
            dp[dep + 1][nextNum] = 1
            dfs(nextNum, dep + 1)

n = int(input())
nums = [*map(int, input().split())]
k = int(input())
make = set(nums)
dp = [[0] * (nums[-1] * k + 1) for _ in range(k + 1)]
dfs(0, 0)
make = sorted(list(make))
for i in range(len(make)):
    if i + 1 != make[i]:
        print(f"{'holsoon' if i % 2 else 'jjaksoon'} win at {i + 1}")
        break
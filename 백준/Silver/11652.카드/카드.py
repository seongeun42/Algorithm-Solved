import sys
input = sys.stdin.readline
N = int(input())
nums = sorted([int(input()) for _ in range(N)])
res = [-1, 0]
while N:
    cnt = 1
    while N > 1 and nums[N - 1] == nums[N - 2]:
        cnt += 1
        N -= 1
    if cnt >= res[0]:
        res = [cnt, nums[N - 1]]
    N -= 1
print(res[1])
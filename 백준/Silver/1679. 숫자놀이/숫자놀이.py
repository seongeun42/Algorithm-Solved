import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([(v, 1) for v in nums])
    for i in range(n):
        dp[1][nums[i]] = 1
    while q:
        cv, cnt = q.popleft()
        if cnt == k:
            continue
        for i in range(n):
            nv = cv + nums[i]
            make.add(nv)
            if dp[cnt + 1][nv] != 1:
                dp[cnt + 1][nv] = 1
                q.append((nv, cnt + 1))

n = int(input())
nums = [*map(int, input().split())]
k = int(input())
make = set(nums)
dp = [[0] * (nums[-1] * k + 1) for _ in range(k + 1)]
bfs()
make = sorted(list(make))
for i in range(len(make)):
    if i + 1 != make[i]:
        print(f"{'holsoon' if i % 2 else 'jjaksoon'} win at {i + 1}")
        break
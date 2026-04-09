from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque([])
nums = {}
for _ in range(N):
    a, b = input().rstrip().split()
    nums[a] = int(b)
    q.append(a)
while len(q) > 1:
    cnt = nums[q.popleft()]
    for _ in range(cnt - 1):
        q.append(q.popleft())
    q.popleft()
print(q.popleft())
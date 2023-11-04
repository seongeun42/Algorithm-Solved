from collections import deque

N = int(input())
nums = [*map(int, input().split())]
q = deque([(-nums[i], i + 1) for i in range(N)])

ans = [1]
rot = q.popleft()[0]
while q:
    q.rotate(rot + 1 if rot < 0 else rot)
    rot, idx = q.popleft()
    ans.append(idx)
print(*ans)
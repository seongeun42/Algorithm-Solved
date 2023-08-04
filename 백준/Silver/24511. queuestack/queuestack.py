import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
ds = [*map(int, input().split())]
ele = [*map(int, input().split())]
q = deque([])
for i in range(n):
    if ds[i] == 0:
        q.appendleft(ele[i])
cnt = int(input())
q.extend([*map(int, input().split())])
print(*list(q)[:cnt])
from collections import deque
import sys, heapq
input = sys.stdin.readline

N = int(input())
q = deque([*map(int,input().split())])
cur = 1
cnt = 0
while q:
    x = q.popleft()
    if x == cur:
        cur += 1
    else:
        cnt += 1
print(cnt)
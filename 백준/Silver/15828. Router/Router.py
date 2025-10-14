from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque([])
while 1:
    p = int(input())
    if p == -1:
        break
    if p > 0 and len(q) < N:
        q.append(p)
    elif p == 0:
        q.popleft()
if q:
    print(*q)
else:
    print("empty")
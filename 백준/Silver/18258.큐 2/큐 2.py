from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    op = input().split()
    if op[0] == "push":
        q.append(op[1])
    elif op[0] == "pop":
        print(q.popleft() if q else -1)
    elif op[0] == "size":
        print(len(q))
    elif op[0] == "empty":
        print(0 if q else 1)
    elif op[0] == "front":
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)
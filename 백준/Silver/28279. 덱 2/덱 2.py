from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque([])
for _ in range(N):
    op = [*map(int, input().split())]
    if op[0] == 1:
        q.appendleft(op[1])
    elif op[0] == 2:
        q.append(op[1])
    elif op[0] == 3:
        print(q.popleft() if q else -1)
    elif op[0] == 4:
        print(q.pop() if q else -1)
    elif op[0] == 5:
        print(len(q))
    elif op[0] == 6:
        print(0 if q else 1)
    elif op[0] == 7:
        print(q[0] if q else -1)
    elif op[0] == 8:
        print(q[-1] if q else -1)
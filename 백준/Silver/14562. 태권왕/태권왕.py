from collections import deque
import sys
input = sys.stdin.readline

def bfs(s, t):
    q = deque([(s, t, 0)])
    while q:
        cs, ct, cnt = q.popleft()
        if cs == ct:
            return cnt
        if cs < ct:
            q.append((cs * 2, ct + 3, cnt + 1))
            q.append((cs + 1, ct, cnt + 1))

C = int(input())
for _ in range(C):
    S, T = map(int, input().split())
    print(bfs(S, T))
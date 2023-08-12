from collections import deque
import sys
input = sys.stdin.readline

def solve():
    N, T, W = map(int, input().split())
    q = deque([])
    notYet = []
    for _ in range(N):
        pi, tx = map(int, input().split())
        q.append([pi, tx, 0])
    M = int(input())
    for _ in range(M):
        pi, tx, ci = map(int, input().split())
        notYet.append([pi, tx, ci])
    notYet.sort(key=lambda x: -x[2])
    i = 0
    while i < W:
        pi, tx, ci = q.popleft()
        for _ in range(min(T, tx)):
            if i >= W: return
            i += 1
            print(pi)
            if notYet and notYet[-1][2] == i:
                q.append(notYet.pop())
        if tx > T:
            q.append([pi, tx - T, ci + T])

solve()
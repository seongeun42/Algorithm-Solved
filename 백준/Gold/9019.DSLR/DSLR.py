import sys
from collections import deque
input = sys.stdin.readline

def D(n):
    return 2*n % 10000

def S(n):
    return n - 1 if n else 9999

def L(n):
    return ((n % 1000) * 10) + (n // 1000)

def R(n):
    return ((n % 10) * 1000) + (n // 10)

def bfs(a, b):
    visit = [0] * 10000
    visit[a] = 1
    q = deque([[a, ""]])
    while q:
        v, res = q.popleft()
        if v == b:
            return res
        n = D(v)
        if not visit[n]:
            visit[n] = 1
            q.append([n, res+"D"])
        n = S(v)
        if not visit[n]:
            visit[n] = 1
            q.append([n, res+"S"])
        n = L(v)
        if not visit[n]:
            visit[n] = 1
            q.append([n, res+"L"])
        n = R(v)
        if not visit[n]:
            visit[n] = 1
            q.append([n, res+"R"])

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(bfs(a, b))
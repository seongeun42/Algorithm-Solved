from sys import stdin
input = stdin.readline

N, X = map(int, input().split())
res = -1
for _ in range(N):
    S, T = map(int, input().split())
    if res < S and S + T <= X:
        res = S
    print(res)
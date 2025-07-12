import sys
input = sys.stdin.readline

N, X, K = map(int, input().split())
ball = X
for _ in range(K):
    A, B = map(int, input().split())
    if ball == A:
        ball = B
    elif ball == B:
        ball = A
print(ball)
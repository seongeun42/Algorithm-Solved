import sys
input = sys.stdin.readline

def solve():
    H, W, X, Y = map(int, input().split())
    B = [[*map(int, input().split())] for _ in range(H + X)]
    A = [[0] * W for _ in range(H)]
    for i in range(X):
        for j in range(W):
            A[i][j] = B[i][j]
    for i in range(H):
        for j in range(Y):
            A[i][j] = B[i][j]
    for i in range(H, H + X):
        for j in range(Y, W + Y):
            A[i - X][j - Y] = B[i][j]
    for i in range(X, H + X):
        for j in range(W, W + Y):
            A[i - X][j - Y] = B[i][j]
    for i in range(X, H):
        for j in range(Y, W):
            A[i][j] = B[i][j] - A[i - X][j - Y]
    for a in A:
        print(*a, sep=" ")

solve()
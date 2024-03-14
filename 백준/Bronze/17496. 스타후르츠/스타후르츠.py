N, T, C, P = map(int, input().split())
cnt = N // T - 1 if N % T == 0 else N // T
print(cnt * C * P)
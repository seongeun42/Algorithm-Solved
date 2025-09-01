A, B, C = map(int, input().split())
i, j, k = map(int, input().split())
v = min(A / i, B / j, C / k)
print(A - i * v, B - j * v, C - k * v)
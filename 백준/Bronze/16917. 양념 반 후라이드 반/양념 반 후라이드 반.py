A, B, C, X, Y = map(int, input().split())
half = C * min(X, Y) * 2
if X > Y:
    half += min(A, C * 2) * (X - Y)
else:
    half += min(B, C * 2) * (Y - X)
print(min(A * X + B * Y, half))
X, Y, W, S = map(int, input().split())
ans = min((X + Y) * W, min(X, Y) * S + abs(X - Y) * W)
if (X + Y) % 2 == 0:
    ans = min(ans, max(X, Y) * S)
else:
    ans = min(ans, (max(X, Y) - 1) * S + W)
print(ans)
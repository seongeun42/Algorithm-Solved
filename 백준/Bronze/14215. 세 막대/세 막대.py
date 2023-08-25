a, b, c = map(int, input().split())
if max(a, b, c) == c:
    c = min(c, a + b - 1)
elif max(a, b, c) == b:
    b = min(b, a + c - 1)
else:
    a = min(a, b + c - 1)
print(a + b + c)
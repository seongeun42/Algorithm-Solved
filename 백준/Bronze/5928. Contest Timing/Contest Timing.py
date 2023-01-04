d, h, m = map(int, input().split())
t = (d * 24 * 60 + h * 60 + m) - (11 * 24 * 60 + 11 * 60 + 11)
print(t if t >= 0 else -1)
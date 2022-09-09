a, b = map(int, input().split())
r = a * ((100 - b) / 100)
print(1 if r < 100 else 0)
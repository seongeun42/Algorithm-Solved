a, b = map(int, input().split())
x = abs((a - 1) // 4 - (b - 1) // 4)
y = abs((a - 1) % 4 - (b - 1) % 4)
print(x + y)
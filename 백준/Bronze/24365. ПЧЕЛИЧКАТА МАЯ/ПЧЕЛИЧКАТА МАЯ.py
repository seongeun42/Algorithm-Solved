a, b, c = map(int, input().split())
avg = (a + b + c) // 3
res = (c - avg)
b += (c - avg)
res += (b - avg)
print(res)
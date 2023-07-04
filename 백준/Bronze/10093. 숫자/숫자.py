a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
n = [i for i in range(a + 1, b)]
print(len(n))
print(*n)
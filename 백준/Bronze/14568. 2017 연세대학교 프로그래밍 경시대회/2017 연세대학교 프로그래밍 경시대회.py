n = int(input())
print(sum([(n - i - 2) // 2 for i in range(2, n - 1, 2)]))
n = int(input())
a, b = map(int, input().split())
print(n if n < a // 2 + b else a // 2 + b)
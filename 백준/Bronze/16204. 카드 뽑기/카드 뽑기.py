n, m, k = map(int, input().split())
print(n - m + k if k <= m else m + n - k)
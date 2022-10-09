n, m = map(int, input().split())
ans = (n // 2 * m) + (m // 2) * (n % 2)
print(ans)
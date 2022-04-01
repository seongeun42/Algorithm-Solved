def fast_pow(n):
    if n == 1:
        return A % C
    v = fast_pow(n // 2)
    if n % 2:
        return v * v * A % C
    else:
        return v * v % C

A, B, C = map(int, input().split())
print(fast_pow(B))
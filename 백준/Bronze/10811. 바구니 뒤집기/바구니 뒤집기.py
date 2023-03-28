n, m = map(int, input().split())
b = [i for i in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    b[i:j + 1] = b[j:i - 1:-1]
print(*b[1:])
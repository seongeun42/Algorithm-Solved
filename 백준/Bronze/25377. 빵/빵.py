n = int(input())
ans = 1001
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b:
        ans = min(ans, b)
print(ans if ans != 1001 else -1)
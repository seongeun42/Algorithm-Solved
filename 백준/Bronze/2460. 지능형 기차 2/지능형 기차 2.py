p = 0
ans = 0
for _ in range(10):
    o, i = map(int, input().split())
    p += -o + i
    ans = max(ans, p)
print(ans)
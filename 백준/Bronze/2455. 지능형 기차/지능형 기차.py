total, ans = 0, 0
for _ in range(4):
    outP, inP = map(int, input().split())
    total += (inP - outP)
    ans = max(ans, total)
print(ans)
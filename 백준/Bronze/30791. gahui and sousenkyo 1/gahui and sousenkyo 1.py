scores = [*map(int, input().split())]
ans = 0
for i in range(1, len(scores)):
    if scores[0] - 1000 <= scores[i]:
        ans += 1
print(ans)
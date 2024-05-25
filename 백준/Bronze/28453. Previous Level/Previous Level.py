N = int(input())
M = [*map(int, input().split())]
ans = []
for v in M:
    if v == 300:
        ans.append(1)
    elif v >= 275:
        ans.append(2)
    elif v >= 250:
        ans.append(3)
    else:
        ans.append(4)
print(*ans)
N = int(input())
snow = sorted([*map(int, input().split())])
ans = 0
while snow:
    if len(snow) == 1:
        ans += snow.pop()
    else:
        b, s = snow.pop(), snow.pop()
        ans += s
        snow.append(b - s)
        snow.sort()
print(ans if ans <= 1440 else -1)
t = [int(input()) for _ in range(5)]
res = 0
if t[0] <= 0:
    res += abs(t[0]) * t[2] + t[3]
res += t[1] * t[4] if t[0] <= 0 else (t[1] - t[0]) * t[4]
print(res)
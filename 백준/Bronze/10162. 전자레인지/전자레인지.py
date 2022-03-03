T = int(input())
res = [0, 0, 0]
for i, v in enumerate([300, 60, 10]):
    res[i], T = divmod(T, v)
if T: print(-1)
else: print(*res)
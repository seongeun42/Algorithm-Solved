m, n = map(int, input().split())
snack = [*map(int, input().split())]
s, e = 1, max(snack)
res = 0
while s <= e:
    mid = (s + e) // 2
    if mid == 0: break
    cnt = sum([l // mid for l in snack])
    if cnt >= m:
        res = max(res, mid)
        s = mid + 1
    else:
        e = mid - 1
print(res)
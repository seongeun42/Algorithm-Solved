n = int(input())
budget = list(map(int, input().split()))
limit = int(input())
start, end = 0, max(budget)
res = 0
while start <= end:
    mid = (start + end) // 2
    b = 0
    for v in budget:
        if v > mid: b += mid
        else: b += v

    if b < limit:
        start = mid + 1
        res = mid
    elif b > limit:
        end = mid - 1
    else:
        res = mid
        break

print(res)
N, M = map(int, input().split())
arr = [*map(int, input().split())]
total_min_v, total_max_v = min(arr), max(arr)
s, e = 0, total_max_v - total_min_v
ans = 0
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    min_v, max_v = arr[0], arr[0]
    for c in arr:
        if c < min_v:
            min_v = c
        if c > max_v:
            max_v = c
        if max_v - min_v >= mid:
            cnt += 1
            min_v, max_v = c, c
    if cnt < M:
        e = mid - 1
    else:
        s = mid + 1
        ans = mid
print(ans)
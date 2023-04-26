n = int(input())
s, e = 1, n
while s <= e:
    mid = (s + e) // 2
    if mid ** 2 == n:
        print(mid)
        break
    if mid ** 2 > n:
        e = mid - 1
    else:
        s = mid + 1
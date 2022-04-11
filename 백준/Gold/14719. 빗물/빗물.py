H, W = map(int, input().split())
B = [*map(int, input().split())]
l_max, r_max = B[0], B[W - 1]
l, r = 0, W - 1
res = 0
while l <= r:
    if l_max < B[l]:
        l_max = B[l]
    else:
        res += l_max - B[l]
    if r_max < B[r]:
        r_max = B[r]
    else:
        res += r_max - B[r]
    if l_max < r_max:
        l += 1
    else:
        r -= 1
print(res)
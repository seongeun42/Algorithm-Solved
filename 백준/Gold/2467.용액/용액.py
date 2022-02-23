N = int(input())
L = [*map(int, input().split())]
res = [2000000001, 0, 0]
l, r = 0, N-1
while l < r:
    v = L[l] + L[r]
    if abs(v) <= res[0]:
        res = [abs(v), l, r]
    if v < 0:
        l += 1
    else:
        r -= 1
print(L[res[1]], L[res[2]])

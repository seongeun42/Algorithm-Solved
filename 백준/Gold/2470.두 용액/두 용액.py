N = int(input())
L = sorted([*map(int, input().split())])
s, e = 0, N - 1
res = [2000000001, 0, 0]
while s < e:
    v = L[s] + L[e]
    if abs(v) < res[0]:
        res = [abs(v), s, e]
    if v < 0:
        s += 1
    else:
        e -= 1
print(L[res[1]], L[res[2]])
n = int(input())
t = list(map(int, input().split()))
sl, sr = [[i, t[i]] for i in range(n)], []
res = [0] * n
while sl:
    sr.append(sl.pop())
    while 1 and sr and sl:
        if sr[-1][1] <= sl[-1][1]:
            v = sr.pop()
            res[v[0]] = len(sl)
        else: break
print(*res, sep=' ')
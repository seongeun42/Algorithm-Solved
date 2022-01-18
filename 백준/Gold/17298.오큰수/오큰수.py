n = int(input())
sl, sr = list(map(int, input().split())), []
res = [-1] * n
for i in range(n):
    v = sl.pop()
    if sr and v >= sr[-1]:
        while sr and v >= sr[-1]:
            sr.pop()
    res[n - i - 1] = sr[-1] if sr else -1
    sr.append(v)
print(*res, sep=' ')
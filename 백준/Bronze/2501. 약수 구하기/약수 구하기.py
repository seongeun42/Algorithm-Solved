def yaksu(n):
    ys = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ys.add(i)
            ys.add(n // i)
    return sorted(list(ys))

n, k = map(int, input().split())
ys = yaksu(n)
print(0 if len(ys) < k else ys[k - 1])
N, K = map(int, input().split())
D = [*map(int, input().split())]
res = sum(D[:K])
hap = res
for i in range(1, N - K + 1):
    hap = hap - D[i - 1] + D[i + K - 1]
    res = max(res, hap)
print(res)
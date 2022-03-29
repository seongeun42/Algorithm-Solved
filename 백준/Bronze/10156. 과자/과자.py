K, N, M = map(int, input().split())
res = K * N - M
print(res if res > 0 else 0)
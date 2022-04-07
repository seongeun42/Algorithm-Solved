N, M = map(int, input().split())
print(abs(N - M) if abs(N - M) > abs(M - N) else abs(M - N))
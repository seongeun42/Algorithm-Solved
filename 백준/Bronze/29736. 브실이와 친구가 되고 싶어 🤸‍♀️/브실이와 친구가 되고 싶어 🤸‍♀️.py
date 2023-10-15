A, B = map(int, input().split())
K, X = map(int, input().split())
minV, maxV = max(A, K - X), min(K + X, B)
cnt = maxV - minV + 1
print(cnt if cnt > 0 else "IMPOSSIBLE")
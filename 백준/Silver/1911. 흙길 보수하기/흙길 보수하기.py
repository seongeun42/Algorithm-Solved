import sys
input = sys.stdin.readline

N, L = map(int, input().split())
W = sorted([[*map(int, input().split())] for _ in range(N)])
cnt, i = 0, W[0][0]
for s, e in W:
    V, M = divmod(e - max(s, i), L)
    cnt = cnt + V if not M else cnt + V + 1
    i = max(i, s)
    i = i + V * L if not M else i + (V + 1) * L
print(cnt)
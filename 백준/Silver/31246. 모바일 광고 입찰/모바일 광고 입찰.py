import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cha = []
cnt = 0
for _ in range(N):
    a, b = map(int, input().split())
    if b <= a:
        cnt += 1
    else:
        cha.append(b - a)
cha.sort()
if cnt < K:
    print(cha[K - cnt - 1])
else:
    print(0)
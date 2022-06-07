import sys
input = sys.stdin.readline

N, P = map(int, input().split())
line = [[] for _ in range(7)]
cnt = 0
for _ in range(N):
    l, plat = map(int, input().split())
    while line[l] and line[l][-1] > plat:
        line[l].pop()
        cnt += 1
    if not line[l] or line[l][-1] != plat:
        line[l].append(plat)
        cnt += 1
print(cnt)
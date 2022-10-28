import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nations = [[*map(int, input().split())] for _ in range(n)]
nations.sort(key=lambda x : (-x[1], -x[2], -x[3]))
for i in range(n):
    if nations[i][0] == k:
        idx = i
for i in range(n):
    if nations[idx][1:] == nations[i][1:]:
        print(i + 1)
        break
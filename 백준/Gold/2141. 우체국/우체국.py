import sys
input = sys.stdin.readline

N = int(input())
village = []
total = 0
for _ in range(N):
    a, b = map(int, input().split())
    total += b
    village.append((a, b))
village.sort()
cnt = 0
for i in range(N):
    cnt += village[i][1]
    if cnt >= total / 2:
        print(village[i][0])
        break
import sys, heapq
input = sys.stdin.readline
N, M, K = map(int, input().split())
beer = sorted([[*map(int, input().split())] for _ in range(K)], key=lambda x: x[1])
drink = []
prefer = 0
find = 0
for i in range(K):
    heapq.heappush(drink, beer[i][0])
    prefer += beer[i][0]
    if len(drink) == N:
        if prefer >= M:
            find = 1
            print(beer[i][1])
            break
        else:
            prefer -= heapq.heappop(drink)
if not find: print(-1)
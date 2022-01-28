import heapq, sys
input = sys.stdin.readline
n = int(input())
hp = []
for _ in range(n):
    v = int(input())
    if v:
        heapq.heappush(hp, [abs(v), v])
    else:
        print(heapq.heappop(hp)[1] if hp else 0)
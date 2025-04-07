import heapq

N = int(input())
snow = [-v for v in [*map(int, input().split())]]
heapq.heapify(snow)
ans = 0
while snow:
    if len(snow) == 1:
        ans += -heapq.heappop(snow)
    else:
        a = -heapq.heappop(snow)
        b = -heapq.heappop(snow)
        ans += b
        heapq.heappush(snow, -(a - b))
print(ans if ans <= 1440 else -1)
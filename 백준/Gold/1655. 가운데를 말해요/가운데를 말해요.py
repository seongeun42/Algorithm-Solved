import sys, heapq
input = sys.stdin.readline

def solve():
    N = int(input())
    maxH = []
    minH = []
    for i in range(N):
        num = int(input())
        if i % 2 == 0:
            heapq.heappush(maxH, -num)
        else:
            heapq.heappush(minH, num)
        if len(minH) > 0 and -maxH[0] > minH[0]:
            maxHR = -heapq.heappop(maxH)
            minHR = heapq.heappop(minH)
            heapq.heappush(maxH, -minHR)
            heapq.heappush(minH, maxHR)
        print(-maxH[0])

solve()
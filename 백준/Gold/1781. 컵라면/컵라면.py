import sys, heapq
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = sorted([[*map(int, input().split())] for _ in range(N)])
    hq = []
    day = 1
    for dead, cup in arr:
        if day <= dead:
            heapq.heappush(hq, cup)
            day += 1
        elif hq[0] < cup:
            heapq.heappop(hq)
            heapq.heappush(hq, cup)
    print(sum(hq))

solve()
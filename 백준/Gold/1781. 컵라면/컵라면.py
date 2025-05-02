import sys, heapq
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = [[*map(int, input().split())] for _ in range(N)]
    arr.sort()
    hq = []
    for dead, cup in arr:
        if len(hq) < dead:
            heapq.heappush(hq, cup)
        elif hq[0] < cup:
            heapq.heappushpop(hq, cup)
    print(sum(hq))

solve()
import sys, heapq
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = sorted([[*map(int, input().split())] for _ in range(N)])
    hq = []
    day, ans = 1, 0
    for dead, cup in arr:
        if day <= dead:
            ans += cup
            heapq.heappush(hq, cup)
            day += 1
        elif hq[0] < cup:
            ans = ans - heapq.heappop(hq) + cup
            heapq.heappush(hq, cup)
    print(ans)

solve()
import sys, heapq
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        hq = [*map(int, input().split())]
        heapq.heapify(hq)
        ans = 1
        while len(hq) > 1:
            a, b = heapq.heappop(hq), heapq.heappop(hq)
            ans *= (a * b)
            ans %= 1_000_000_007
            heapq.heappush(hq, a * b)
        print(ans)

solve()
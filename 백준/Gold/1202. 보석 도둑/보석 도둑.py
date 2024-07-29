import sys, heapq
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    jew = [[*map(int, input().split())] for _ in range(N)]
    heapq.heapify(jew)
    bag = sorted([int(input()) for _ in range(K)])
    ans = 0
    tmp = []
    for c in bag:
        while jew and c >= jew[0][0]:
            heapq.heappush(tmp, -heapq.heappop(jew)[1])
        if tmp:
            ans -= heapq.heappop(tmp)
        if not jew and not tmp:
            break
    print(ans)

solve()
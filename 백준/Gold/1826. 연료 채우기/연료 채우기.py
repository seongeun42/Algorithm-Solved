import sys, heapq
input = sys.stdin.readline

def solve():
    n = int(input())
    stations = sorted([[*map(int, input().split())] for _ in range(n + 1)])
    stations[-1][1], tank = 0, stations[-1][1]
    gas = []
    ans = 0
    cur = 0
    for dist, amount in stations:
        need = dist - cur
        while gas and tank < need:
            v = -heapq.heappop(gas)
            tank += v
            ans += 1
        if not gas and tank < need:
            print(-1)
            return
        cur = dist
        tank -= need
        heapq.heappush(gas, -amount)
    print(ans)

solve()
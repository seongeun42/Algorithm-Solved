import sys, heapq
input = sys.stdin.readline

def find_root(n, R):
    if R[n] != n:
        R[n] = find_root(R[n], R)
    return R[n]

def solve():
    n = int(input())
    proposals = []
    for _ in range(n):
        p, d = map(int, input().split())
        heapq.heappush(proposals, (-p, d))
    R = [i for i in range(10001)]
    ans = 0
    while proposals:
        p, d = heapq.heappop(proposals)
        r = find_root(d, R)
        if r > 0:
            ans += -p
            nxt = find_root(r - 1, R)
            R[r] = nxt
    print(ans)

solve()
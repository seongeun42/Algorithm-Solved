import sys, heapq, math
input = sys.stdin.readline

def solve():
    N, H, T = map(int, input().split())
    hq = []
    for _ in range(N):
        heapq.heappush(hq, -1 * int(input()))
    use = 0
    for _ in range(T):
        if H > -hq[0] or -hq[0] == 1:
            break
        tall = -heapq.heappop(hq)
        heapq.heappush(hq, -math.floor(tall / 2))
        use += 1
    if H > -hq[0]:
        print("YES", use, sep="\n")
    else:
        print("NO", -int(hq[0]), sep="\n")

solve()
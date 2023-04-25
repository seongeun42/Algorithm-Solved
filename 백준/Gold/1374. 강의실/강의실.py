import sys, heapq
input = sys.stdin.readline

n = int(input())
wait = []
for _ in range(n):
    r, s, e = map(int, input().split())
    heapq.heappush(wait, (s, e, r))
lec = []
res = 0
while wait:
    s, e, r = heapq.heappop(wait)
    if not lec or s < lec[0][0]:
        res += 1
    elif s >= lec[0][0]:
        heapq.heappop(lec)
    heapq.heappush(lec, (e, s, r))
print(res)
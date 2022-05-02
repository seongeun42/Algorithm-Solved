import sys, heapq
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    nums = [*map(int, input().split())]
    if not q:
        for num in nums:
            heapq.heappush(q, num)
    else:
        for num in nums:
            if q[0] < num:
                heapq.heappush(q, num)
                heapq.heappop(q)
print(q[0])
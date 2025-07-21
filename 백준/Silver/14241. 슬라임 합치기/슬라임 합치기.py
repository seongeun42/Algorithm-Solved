import heapq

N = int(input())
size = [-v for v in map(int, input().split())]
heapq.heapify(size)
score = 0
while len(size) > 1:
    a, b = heapq.heappop(size), heapq.heappop(size)
    score += a * b
    heapq.heappush(size, a + b)
print(score)
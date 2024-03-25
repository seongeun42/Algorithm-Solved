import sys, heapq
input = sys.stdin.readline

N = int(input())
card = [int(input()) for _ in range(N)]
heapq.heapify(card)
cnt = 0
while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    cnt += a + b
    heapq.heappush(card, a + b)
print(cnt)
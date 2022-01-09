n, m = map(int, input().split())
c = list(map(int, input().split()))


# 정렬로 푼 코드
for _ in range(m):
  c = sorted(c)
  c[0], c[1] = c[0] + c[1], c[0] + c[1]
print(sum(c))


# 우선순위큐로 푼 코드
hq.heapify(c)
for _ in range(m):
  v1, v2 = hq.heappop(c), hq.heappop(c)
  hq.heappush(c, v1 + v2)
  hq.heappush(c, v1 + v2)
print(sum(c))

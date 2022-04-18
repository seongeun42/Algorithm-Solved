N, M = map(int, input().split())
loca = [*map(int, input().split())]
left = sorted([abs(v) for v in loca if v < 0], reverse=True)
right = sorted([v for v in loca if v > 0], reverse=True)
dist = []
for i in range(0, len(left), M):
    dist.append(left[i])
for i in range(0, len(right), M):
    dist.append(right[i])
dist.sort()
print(dist.pop() + sum(dist) * 2)
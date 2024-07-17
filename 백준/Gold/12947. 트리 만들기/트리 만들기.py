N = int(input())
cnt = [*map(int, input().split())]
max_edge, seperated = 0, 0
for v in cnt:
    max_edge += 1
    if v == 1:
        max_edge = max(max_edge, seperated + 1)
        seperated = 0
    else:
        seperated += 2
print(max(max_edge, seperated))
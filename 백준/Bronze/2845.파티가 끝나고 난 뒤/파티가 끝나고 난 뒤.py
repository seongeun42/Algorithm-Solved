L, P = map(int, input().split())
cnt = [*map(int, input().split())]
for v in cnt:
    print(v - L * P, end=' ')
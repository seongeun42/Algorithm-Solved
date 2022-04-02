D = int(input())
C = [*map(int, input().split())]
cnt = 0
for v in C:
    if D == v:
        cnt += 1
print(cnt)
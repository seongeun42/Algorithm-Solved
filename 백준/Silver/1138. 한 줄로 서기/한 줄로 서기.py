N = int(input())
record = [*map(int, input().split())]
order = [-1] * N
for i in range(N):
    cnt = 0
    for d in range(N):
        if cnt == record[i] and order[d] == -1:
            order[d] = i + 1
            break
        if order[d] == -1 or order[d] > i + 1:
            cnt += 1
print(*order)
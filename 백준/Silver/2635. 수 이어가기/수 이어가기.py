n = int(input())
maxCnt = 0
record = []
for i in range(1, n + 2):
    pre, next = n, i
    cnt, tmp = 1, [pre]
    while next >= 0:
        tmp.append(next)
        pre, next = next, pre - next
        cnt += 1
    if cnt > maxCnt:
        maxCnt = cnt
        record = tmp
print(maxCnt)
print(*record)
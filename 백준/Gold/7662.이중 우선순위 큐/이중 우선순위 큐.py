import heapq, sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    mmq, mxq = [], []
    notDel = [0] * n
    for i in range(n):
        op, v = input().split()
        if op == 'I':
            heapq.heappush(mmq, [int(v), i])
            heapq.heappush(mxq, [-int(v), i])
            notDel[i] = 1
        elif int(v) == 1:
            while mxq and not notDel[mxq[0][1]]:
                heapq.heappop(mxq)
            if mxq:
                notDel[mxq[0][1]] = 0
                heapq.heappop(mxq)
        else:
            while mmq and not notDel[mmq[0][1]]:
                heapq.heappop(mmq)
            if mmq:
                notDel[mmq[0][1]] = 0
                heapq.heappop(mmq)

    while mxq and not notDel[mxq[0][1]]:
        heapq.heappop(mxq)
    while mmq and not notDel[mmq[0][1]]:
        heapq.heappop(mmq)

    if mxq and mmq:
        print(-mxq[0][0], mmq[0][0], sep=' ')
    else:
        print("EMPTY")
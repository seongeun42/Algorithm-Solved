import sys
input = sys.stdin.readline

N, M = map(int, input().split())
title = sorted([[*input().split()] for _ in range(N)], key=lambda x: int(x[1]))
for _ in range(M):
    v = int(input())
    s, e = 0, N - 1
    idx = 0
    while s <= e:
        mid = (s + e) // 2
        if v > int(title[mid][1]):
            s = mid + 1
        else:
            idx = mid
            e = mid - 1
    print(title[idx][0])
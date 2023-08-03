import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    aisle = [0] * 200
    for _ in range(N):
        s, t = map(int, input().split())
        if s % 2: s += 1
        if t % 2: t += 1
        start = min(s, t) // 2 - 1
        end = abs(s - t) // 2 + 1 + start
        for i in range(start, end):
            aisle[i] += 1
    print(max(aisle) * 10)
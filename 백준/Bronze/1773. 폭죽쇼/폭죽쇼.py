import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = [0] * (C + 1)
time = [int(input()) for _ in range(N)]
for t in time:
    if t == 1:
        print(C)
        break
    for c in range(t, C + 1, t):
        arr[c] = 1
else:
    print(sum(arr))
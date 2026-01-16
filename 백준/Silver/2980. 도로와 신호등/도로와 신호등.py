import sys
input = sys.stdin.readline

N, L = map(int, input().split())
sign = [[*map(int, input().split())] for _ in range(N)]
loca, time = 0, 0
for i in range(N):
    D, R, G = sign[i]
    time += D - loca
    loca = D
    if time % (R + G) < R:
        time += R - (time % (R + G))
time += L - loca
print(time)
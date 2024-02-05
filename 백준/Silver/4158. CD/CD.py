import sys
input = sys.stdin.readline

while 1:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    sg = set([int(input()) for _ in range(N)])
    sy = set([int(input()) for _ in range(M)])
    print(len(sg & sy))
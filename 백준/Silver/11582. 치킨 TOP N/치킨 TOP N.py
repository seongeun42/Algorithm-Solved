import sys
input = sys.stdin.readline

N = int(input())
score = [*map(int, input().split())]
k = int(input())
cnt = N // k
for i in range(0, N, cnt):
    print(*sorted(score[i:i+cnt]), end=" ")
import sys
input = sys.stdin.readline

N = int(input())
a = [*map(int, input().split())]
hap = [0]
for i in range(N):
    hap.append(hap[i] + a[i])
M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    print(hap[max(i, j)] - hap[min(i, j) - 1])
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
wall = [1] * (N - 1)
for _ in range(M):
    x, y = map(int, input().split())
    for i in range(x - 1, y - 1):
        wall[i] = 0
print(1 + sum(wall))
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
flag = 1
for _ in range(M):
    kn = int(input())
    k = [*map(int, input().split())]
    if k != sorted(k, reverse=True):
        flag = 0
print("Yes" if flag else "No")
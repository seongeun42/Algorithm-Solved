import sys
input = sys.stdin.readline

M = int(input())
cup = {1: 1, 2: 2, 3: 3}
for _ in range(M):
    x, y = map(int, input().split())
    cup[x], cup[y] = cup[y], cup[x]
for k, v in cup.items():
    if v == 1:
        print(k)
        break
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    type = {}
    cnt = 1
    for _ in range(n):
        nm, tp = input().split()
        if tp in type: type[tp] += 1
        else: type[tp] = 2
    for k, v in type.items():
        cnt *= v
    print(cnt - 1)
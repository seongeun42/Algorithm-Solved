import sys
input = sys.stdin.readline
n = [0] * 31
for _ in range(28):
    n[int(input())] = 1
for i in range(1, 31):
    if n[i] == 0:
        print(i)
import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
stack = [0]
res = [-1] * n

for i in range(len(a)):
    while stack and a[i] > a[stack[-1]]:
        res[stack.pop()] = a[i]
    stack.append(i)

print(" ".join(map(str, res)))

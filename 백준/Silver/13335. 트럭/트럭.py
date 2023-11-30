from collections import deque
import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())
a = deque([*map(int, input().split())])
out = deque([])
time = 0
weight = 0
while len(a) + len(out) != 0:
    if out and time - out[0][1] == w:
        weight -= out.popleft()[0]
    if a and weight + a[0] <= L:
        out.append([a.popleft(), time])
        weight += out[-1][0]
    time += 1
print(time)
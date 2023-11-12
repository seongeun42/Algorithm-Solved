import sys
input = sys.stdin.readline

N = int(input())
xlist, ylist = [], []
for _ in range(N):
    x, y = map(int, input().split())
    xlist.append(x)
    ylist.append(y)
print((max(xlist) - min(xlist)) * (max(ylist) - min(ylist)))
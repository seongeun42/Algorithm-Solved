import sys
input = sys.stdin.readline

while 1:
    a, b = sorted(map(int, input().split()), reverse=True)
    if a == b == 0:
        break
    print(b * 2 - a)
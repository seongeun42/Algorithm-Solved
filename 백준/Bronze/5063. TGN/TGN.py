import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    r, e, c = map(int, input().split())
    if e - c > r:
        print("advertise")
    elif e - c < r:
        print("do not advertise")
    else:
        print("does not matter")
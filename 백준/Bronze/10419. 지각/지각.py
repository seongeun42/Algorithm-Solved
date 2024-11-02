import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    d = int(input())
    for i in range(d + 1):
        if i + i ** 2 > d:
            print(i - 1)
            break
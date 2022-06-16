import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    total = 0
    for _ in range(N):
        total += int(input())
    if total == 0:
        print(0)
    else:
        print('-' if total < 0 else '+')
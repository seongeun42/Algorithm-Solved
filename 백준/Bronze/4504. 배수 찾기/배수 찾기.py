import sys
input = sys.stdin.readline
n = int(input())
while 1:
    num = int(input())
    if num == 0:
        break
    print(f"{num} is{'' if num % n == 0 else ' NOT'} a multiple of {n}.")
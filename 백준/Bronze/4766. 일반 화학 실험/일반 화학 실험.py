import sys
input = sys.stdin.readline

pre = float(input())
while 1:
    tmp = float(input())
    if tmp == 999:
        break
    print(f'{tmp - pre:.2f}')
    pre = tmp
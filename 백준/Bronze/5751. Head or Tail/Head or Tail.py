import sys
input = sys.stdin.readline

while 1:
    n = int(input())
    if n == 0:
        break
    arr = list(input().rstrip().split())
    M, J = 0, 0
    for v in arr:
        if v == '0':
            M += 1
        else:
            J += 1
    print(f"Mary won {M} times and John won {J} times")
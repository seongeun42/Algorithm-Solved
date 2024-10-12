import sys
input = sys.stdin.readline

while 1:
    n = list(input().strip())
    if n[0] == '0':
        break
    while len(n) > 1:
        n = list(str(sum(map(int, n))))
    print(''.join(n))
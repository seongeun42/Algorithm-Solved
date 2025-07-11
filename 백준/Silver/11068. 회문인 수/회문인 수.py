import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = int(input())
    for b in range(2, 65):
        num = s
        tmp = []
        while num > 0:
            num, a = divmod(num, b)
            tmp.append(a)
        if tmp == tmp[::-1]:
            print(1)
            break
    else:
        print(0)
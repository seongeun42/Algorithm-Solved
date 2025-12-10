from math import pi
n = int(input())
for _ in range(n):
    a1,p1 = map(int,input().split())
    a2,p2 = map(int,input().split())
    if a1/p1 > a2**2*pi/p2:
        print('Slice of pizza')
    else:
        print('Whole pizza')
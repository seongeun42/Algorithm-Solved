import math
N = int(input())
R = [*map(int, input().split())]
for i in range(1, N):
    gcd = math.gcd(R[0], R[i])
    print(R[0]//gcd, "/", R[i]//gcd, sep='')
import math
N, M = map(int, input().split())
if N == M == 0:
    print(0)
elif math.gcd(N, M) == 1:
    print(1)
else:
    print(2)
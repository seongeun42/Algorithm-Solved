import math
N, M = map(int, input().split())
if N == M == 0:
    print(0)
else:
    print(1 if math.gcd(N, M) == 1 else 2)
import math
N, S = map(int, input().split())
A = [*map(int, input().split())]
if N == 1:
    print(abs(A[0] - S))
else:
    C = [abs(v - S) for v in A]
    res = math.gcd(C[0], C[1])
    for i in range(2, N):
        res = math.gcd(res, C[i])
    print(res)
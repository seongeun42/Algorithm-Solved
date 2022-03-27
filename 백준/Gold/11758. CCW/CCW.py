A = [*map(int, input().split())]
B = [*map(int, input().split())]
C = [*map(int, input().split())]
v = (B[0] - A[0]) * (C[1] - A[1]) - (C[0] - A[0]) * (B[1] - A[1])
if v == 0:
    print(0)
elif v > 0:
    print(1)
else:
    print(-1)
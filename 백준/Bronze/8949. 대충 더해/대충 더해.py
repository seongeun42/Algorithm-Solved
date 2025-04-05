A, B = input().split()
al, bl = len(A), len(B)
if al > bl:
    B = '0' * (al - bl) + B
elif al < bl:
    A = '0' * (bl - al) + A
for i in range(len(A)):
    print(int(A[i]) + int(B[i]), end='')
k = int(input())
A, B = 1, 0
for _ in range(k):
    A, B = B, A + B
print(A, B)
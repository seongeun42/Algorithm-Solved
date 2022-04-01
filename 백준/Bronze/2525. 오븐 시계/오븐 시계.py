A, B = map(int, input().split())
C = int(input())
up, B = divmod(B + C, 60)
A = (A + up) % 24
print(A, B)
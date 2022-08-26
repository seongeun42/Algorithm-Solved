X = int(input())
N = int(input())
tt = 0
for _ in range(N):
    a, b = map(int, input().split())
    tt += a * b
print("Yes" if X == tt else "No")
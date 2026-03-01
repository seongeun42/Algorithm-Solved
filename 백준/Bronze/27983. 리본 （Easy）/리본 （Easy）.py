N = int(input())
X = [*map(int, input().split())]
L = [*map(int, input().split())]
C = list(input().split())
for i in range(N):
    for j in range(i + 1, N):
        if abs(X[i] - X[j]) <= L[i] + L[j] and C[i] != C[j]:
            print("YES")
            print(i + 1, j + 1)
            exit()
print("NO")
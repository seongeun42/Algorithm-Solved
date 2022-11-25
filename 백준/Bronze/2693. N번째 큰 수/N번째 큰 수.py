t = int(input())
for _ in range(t):
    A = sorted([*map(int, input().split())], reverse=True)
    print(A[2])
    
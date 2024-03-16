N = int(input())
A = [*map(int, input().split())]
B = [*map(int, input().split())]
print(sum([1 for i in range(N) if A[i] <= B[i]]))
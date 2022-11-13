N = int(input())
A = [*map(int, input().split())]
A = sorted([[A[i], i, 0] for i in range(N)], key=lambda x: [x[0], x[1]])
for i in range(N):
    A[i][2] = i
A.sort(key=lambda x: [x[1]])
print(*list(zip(*A))[2])
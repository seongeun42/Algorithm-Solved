N = int(input())
C = [[*map(int, input().split())] for _ in range(N)]
for i in range(1, N):
    C[i][0] += min(C[i-1][1], C[i-1][2])
    C[i][1] += min(C[i-1][0], C[i-1][2])
    C[i][2] += min(C[i-1][0], C[i-1][1])
print(min(C[-1]))
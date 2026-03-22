N = int(input())
V = [*map(int, input().split())] + [0]
ans = 0
for i in range(N - 1, -1, -1):
    if V[i + 1] + 1 < V[i]:
        V[i] = V[i + 1] + 1
    ans += V[i]
print(ans)
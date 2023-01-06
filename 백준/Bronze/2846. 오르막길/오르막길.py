n = int(input())
ns = [*map(int, input().split())]
start = 0
ans = 0
for i in range(1, n):
    if ns[i - 1] < ns[i]:
        ans = max(ans, ns[i] - ns[start])
    else:
        start = i
print(ans)
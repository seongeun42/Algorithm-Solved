n = int(input())
p = [*map(int, input().split())]
ans = []
for i in range(n):
    ans.insert(i - p[i], i + 1)
for i in ans:
    print(i, end=" ")
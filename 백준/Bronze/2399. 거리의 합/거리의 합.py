n = int(input())
x = sorted([*map(int, input().split())])
ans = sum([x[i] * (2 * i - n + 1) for i in range(n)])
print(2 * ans)
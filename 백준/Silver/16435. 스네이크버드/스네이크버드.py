n, l = map(int, input().split())
h = sorted([*map(int, input().split())])
for i in range(n):
    if h[i] <= l:
        l += 1
print(l)
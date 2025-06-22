N = int(input())
arr = [*map(int, input().split())]
total = sum(arr)
res = 0
for n in arr:
    total -= n
    res += total * n
print(res)
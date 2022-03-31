N = int(input())
M = int(input())
res = abs(N - 100)
broke = set(input().split()) if M else set()
for i in range(1000001):
    if not set(list(str(i))) & broke:
        res = min(res, len(str(i)) + abs(N - i))
print(res)
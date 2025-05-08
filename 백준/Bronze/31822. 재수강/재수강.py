code = input()
N = int(input())
res = 0
for _ in range(N):
    if code[:5] == input()[:5]:
        res += 1
print(res)
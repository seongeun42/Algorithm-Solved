_, A = input(), [*map(int, input().split())]
sosu = [True] * (max(A) + 1)
sosu[0], sosu[1] = False, False
for i in range(2, int(len(sosu) ** 0.5) + 1):
    if sosu[i]:
        for j in range(i + i, len(sosu), i):
            sosu[j] = False
s = set()
for v in A:
    if sosu[v]:
        s.add(v)
if len(s) > 0:
    ans = 1
    for v in s:
        ans *= v
    print(ans)
else:
    print(-1)
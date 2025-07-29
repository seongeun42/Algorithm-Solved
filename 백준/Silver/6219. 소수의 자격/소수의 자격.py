A, B, D = map(int, input().split())
sosu = [True] * (B + 1)
sosu[0], sosu[1] = False, False
for i in range(2, int(B ** 0.5) + 1):
    if sosu[i]:
        for j in range(i + i, B + 1, i):
            sosu[j] = False
ans = 0
D = str(D)
for i in range(A, B):
    if sosu[i] and D in str(i):
        ans += 1
print(ans)
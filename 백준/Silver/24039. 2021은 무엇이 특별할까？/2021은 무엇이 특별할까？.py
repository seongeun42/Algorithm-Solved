N = int(input())
sosu = []
chk = [False, False] + [True] * (10 * N)
for i in range(2, int(10 * N ** 0.5) + 1):
    if chk[i]:
        sosu.append(i)
        for j in range(i + i, 10 * N, i):
            chk[j] = False
for i in range(1, len(sosu)):
    if N < sosu[i - 1] * sosu[i]:
        print(sosu[i - 1] * sosu[i])
        break
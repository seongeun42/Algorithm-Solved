K = int(input())
num = 10**7
sosu = [1] * num
for i in range(2, int(num**0.5) + 1):
    if sosu[i]:
        for j in range(i + i, num, i):
            sosu[j] = False
sosu = [i for i in range(2, num) if sosu[i]]
print(sosu[K - 1])
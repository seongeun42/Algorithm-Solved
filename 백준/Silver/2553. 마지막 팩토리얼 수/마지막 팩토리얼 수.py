N = int(input())
num = 1
for i in range(1, N + 1):
    num *= i
    while num % 10 == 0:
        num //= 10
    num %= 10**9
print(num % 10)
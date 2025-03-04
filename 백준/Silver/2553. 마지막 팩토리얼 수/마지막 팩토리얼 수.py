N = int(input())
num = 1
for i in range(1, N + 1):
    num *= i
    num = int(str(num).rstrip('0'))
    num %= 10**9
print(num % 10)
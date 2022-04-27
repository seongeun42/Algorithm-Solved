N = int(input())
res = 1
for i in range(2, N + 1):
    res = (res * i) % int(1e13)
    while res % 10 == 0:
        res //= 10
print(str(res)[-5:])
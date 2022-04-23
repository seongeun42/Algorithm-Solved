D, K = map(int, input().split())
p, q = 1, 1
for i in range(4, D + 1):
    p, q = q, p + q
a = 0
while 1:
    a += 1
    if (K - (p * a)) % q == 0:
        print(a)
        print((K - (p * a)) // q)
        break
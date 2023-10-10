N = int(input())
nf = 1
for i in range(1, N + 1):
    nf *= i
week = 7 * 24 * 60 * 60
print(nf // week)
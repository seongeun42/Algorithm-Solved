N, K, A, B = map(int, input().split())
pot = [K] * N
day = 0
while 1:
    if pot[0] == 0:
        break
    day += 1
    for i in range(A):
        pot[i] += B - 1
    for i in range(A, N):
        pot[i] -= 1
    pot.sort()
print(day)
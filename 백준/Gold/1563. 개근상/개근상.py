n = int(input())
OLA = [(0, 0, 0), (1, 1, 1)]
for i in range(2, n + 1):
    O = sum(OLA[i - 1])
    L = 0
    if i <= 3:
        L = OLA[i - 1][0] + OLA[i - 1][2] - OLA[i - 2][1] * 2 
    else:
        L = OLA[i - 1][1] + OLA[i - 2][1] + OLA[i - 3][1]
    A = OLA[i - 1][0] + OLA[i - 1][1] + OLA[i - 2][0] + OLA[i - 2][1]
    if i == 2:
        A += OLA[i - 1][2]
    OLA.append((O, L, A))
print(sum(OLA[n]) % 1000000)
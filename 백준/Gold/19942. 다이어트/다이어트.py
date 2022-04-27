from itertools import combinations as combi

N = int(input())
stand = [*map(int, input().split())]
I = [[i] + [*map(int, input().split())] for i in range(1, N + 1)]
cost, res = 1e9, []
for i in range(1, N + 1):
    for c in combi(I, i):
        flag = 1
        ipfsvc = list(zip(*c))
        for j in range(1, 5):
            if sum(ipfsvc[j]) < stand[j - 1]:
                flag = 0
                break
        if flag:
            tmp = sum(ipfsvc[5])
            if tmp < cost:
                cost, res = tmp, ipfsvc[0]
            if tmp == cost and ipfsvc[0] < res:
                cost, res = tmp, ipfsvc[0]

if cost != 1e9:
    print(cost)
    print(*res, sep=' ')
else:
    print(-1)
T = int(input())
n = [int(input()) for _ in range(T)]
max_n = max(n)
num = [1] * 10
res = [0, 10]
for _ in range(2, max_n + 1):
    tmp = num[:]
    num[0] = tmp[7]
    num[1] = tmp[2] + tmp[4]
    num[2] = tmp[1] + tmp[3] + tmp[5]
    num[3] = tmp[2] + tmp[6]
    num[4] = tmp[1] + tmp[5] + tmp[7]
    num[5] = tmp[2] + tmp[4] + tmp[6] + tmp[8]
    num[6] = tmp[3] + tmp[5] + tmp[9]
    num[7] = tmp[0] + tmp[4] + tmp[8]
    num[8] = tmp[5] + tmp[7] + tmp[9]
    num[9] = tmp[6] + tmp[8]
    res.append(sum(num))
for v in n:
    print(res[v] % 1234567)
from itertools import permutations
n = int(input())
a = list(map(int, input().split()))
o = list(map(int, input().split()))
op = ['+'] * o[0] + ['-'] * o[1] + ['*'] * o[2] + ['//'] * o[3]
opc = set(permutations(op, n - 1))
res = []
for v in opc:
    t = a[0]
    for i in range(1, n):
        if v[i - 1] == '+':
            t += a[i]
        elif v[i - 1] == '-':
            t -= a[i]
        elif v[i - 1] == '*':
            t *= a[i]
        else: t = int(t / a[i])
    res.append(t)
print(max(res), min(res), sep='\n')
n = int(input())
x = list(map(int, input().split()))
xs = sorted(set(x))
dic = { xs[i]: i for i in range(len(xs)) }
for v in x:
    print(dic[v], end=' ')
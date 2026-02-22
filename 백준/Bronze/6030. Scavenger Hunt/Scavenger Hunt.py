P, Q = map(int, input().split())
x, y = [], []
for i in range(1, P + 1):
    if P % i == 0:
        x.append(i)
for i in range(1, Q + 1):
    if Q % i == 0:
        y.append(i)
for v in x:
    for c in y:
        print(v, c)
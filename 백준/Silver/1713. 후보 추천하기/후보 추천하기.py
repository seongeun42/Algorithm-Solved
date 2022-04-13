N = int(input())
T = int(input())
R = [*map(int, input().split())]
P = []
order = 0
for v in R:
    P.sort(key=lambda x: (-x[0], -x[1]))
    flag = 0
    for candi in P:
        if candi[2] == v:
            candi[0] += 1
            flag = 1
            break
    if not flag:
        if len(P) == N:
            P.pop()
            P.append([1, order, v])
        else:
            P.append([1, order, v])
        order += 1
P.sort(key=lambda x: x[2])
for v in P:
    print(v[2], end=' ')
chk = [False, False] + [True] * 1000000
for i in range(1001):
    if chk[i]:
        for j in range(i + i, 1000001, i):
            chk[j] = False
sosu = [i for i, v in enumerate(chk) if v]

N = int(input())
for _ in range(N):
    S = int(input())
    for v in sosu:
        if S % v == 0:
            print("NO")
            break
    else:
        print("YES")
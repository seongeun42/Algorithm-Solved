A, B = map(int, input().split())

sosu = []
counting = [1] * (B + 1)
counting[0], counting[1] = 0, 0
for i in range(2, int(B ** 0.5) + 1):
    if counting[i]:
        sosu.append(i)
        for j in range(i + i, B + 1, i):
            counting[j] = 0

ans = 0
for n in range(A, B + 1):
    num = n
    if counting[n] == 1:
        continue
    i = 0
    cnt = 0
    while n > 1:
        if counting[n]:
            cnt += counting[n]
            break
        else:
            if n % sosu[i] == 0:
                cnt += 1
                n //= sosu[i]
            else:
                i += 1
    counting[num] = cnt
    if counting[cnt] == 1:
        ans += 1
print(ans)
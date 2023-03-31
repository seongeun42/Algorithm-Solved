N = int(input())
ans = 0
hap = 0
s, e = 0, 0
while e <= N:
    if  hap == N:
        ans += 1
        e += 1
        hap += e
    elif hap < N:
        e += 1
        hap += e
    else:
        hap -= s
        s += 1
print(ans)
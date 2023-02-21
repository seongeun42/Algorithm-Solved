n = int(input())
fc = [*map(int, input().split())]
cc = int(input())
ans = 0
for i in range(n):
    if fc[i] > cc:
        ans += (fc[i] // cc + 1) * cc if fc[i] % cc else (fc[i] // cc) * cc
    elif 0 < fc[i] <= cc:
        ans += cc
print(ans)
A, B = input().split()
ca = [0] * 10
cb = [0] * 10
for a in A:
    ca[int(a)] += 1
for b in B:
    cb[int(b)] += 1
ans = 0
for i in range(10):
    for j in range(10):
        ans += i * ca[i] * j * cb[j]
print(ans)
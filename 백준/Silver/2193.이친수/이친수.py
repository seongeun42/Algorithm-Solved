N = int(input())
a = [0, 1, 1]
for i in range(3, 91):
    a.append(a[i-1]+a[i-2])
print(a[N])
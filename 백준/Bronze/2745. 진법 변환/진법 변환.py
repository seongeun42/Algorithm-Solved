n, b = input().split()
n = n[::-1]
b = int(b)
num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = 0
for i in range(len(n)):
    ans += num.find(n[i]) * (b ** i)
print(ans)
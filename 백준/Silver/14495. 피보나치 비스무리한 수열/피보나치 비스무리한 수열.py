n = int(input())
num = [1, 1, 1, 1]
for i in range(4, n + 1):
    num.append(num[i - 1] + num[i - 3])
print(num[n])
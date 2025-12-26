num = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for i in range(2, 10):
    for j in range(2, 10):
        num.add(i * j)
print(1 if int(input()) in num else 0)
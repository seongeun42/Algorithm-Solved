n = int(input())
five, n = divmod(n, 5)
two, n = divmod(n, 2)
while n != 0 and five >= 0:
    n = n + 5 + two * 2
    five -= 1
    two, n = divmod(n, 2)
print(five + two if five >= 0 else -1)
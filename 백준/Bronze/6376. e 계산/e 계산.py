def fac(n):
    if n <= 1:
        return 1
    return n * fac(n - 1)

print("n e")
print("- -----------")
sum = 0.0
for i in range(10):
    sum += 1 / fac(i)
    if i == 0 or i == 1:
        print(f"{i} {int(sum)}")
    elif i == 2:
        print(f"{i} {round(sum, 9)}")
    else:
        print(f"{i} {sum:.9f}")
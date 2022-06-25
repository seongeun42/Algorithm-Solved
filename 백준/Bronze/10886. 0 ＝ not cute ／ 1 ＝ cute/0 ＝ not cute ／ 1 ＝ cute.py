n = int(input())
no, yes = 0, 0
for _ in range(n):
    if int(input()):
        yes += 1
    else:
        no += 1
print("Junhee is not cute!" if no > yes else "Junhee is cute!")
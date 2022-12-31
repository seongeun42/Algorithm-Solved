n = int(input()) // 5
p = int(input())
if n == 0:
    print(p)
elif n == 1:
    print(p - 500 if p > 500 else 0)
elif n == 2:
    if int(p * 0.1) > 500:
        print(int(p * 0.9) if p > int(p * 0.1) else 0)
    else:
        print(p - 500 if p > 500 else 0)
elif n == 3:
    if int(p * 0.1) > 2000:
        print(int(p * 0.9) if p > int(p * 0.1) else 0)
    else:
        print(p - 2000 if p > 2000 else 0)
else:
    if int(p * 0.25) > 2000:
        print(int(p * 0.75) if p > int(p * 0.25) else 0)
    else:
        print(p - 2000 if p > 2000 else 0)
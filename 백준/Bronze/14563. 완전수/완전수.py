T = int(input())
N = [*map(int, input().split())]
for v in N:
    sum = 0
    for i in range(1, v):
        if v % i == 0:
            sum += i
    if sum == v:
        print("Perfect")
    elif sum > v:
        print("Abundant")
    else:
        print("Deficient")
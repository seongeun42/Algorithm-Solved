import sys
input = sys.stdin.readline

nums = [0, 0] + [1] * 999999
for i in range(2, 1001):
    if nums[i]:
        for j in range(i + i, 1000001, i):
            nums[j] = 0

sosu = []
for i in range(3, 1000001):
    if nums[i]:
        sosu.append(i)

while 1:
    n = int(input())
    if n == 0: break
    isPossible = False
    for a in sosu:
        if nums[n - a]:
            print(f"{n} = {a} + {n - a}")
            isPossible = True
            break
    if not isPossible:
        print("Goldbach's conjecture is wrong.")
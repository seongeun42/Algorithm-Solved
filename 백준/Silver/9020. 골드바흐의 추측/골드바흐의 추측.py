nums = [0, 0] + [1] * 9999
for i in range(2, 101):
    if nums[i]:
        for j in range(i + i, 10001, i):
            nums[j] = 0

T = int(input())
for _ in range(T):
    n = int(input())
    A, B = n // 2, n // 2
    for _ in range(10000):
        if nums[A] and nums[B]:
            print(A, B)
            break
        A -= 1
        B += 1
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    op = list(input().strip())
    n = int(input().strip())
    nums = input().strip('[]\n')
    if nums: nums = list(map(int, nums.split(',')))
    pb = True
    pre, back = 0, 0
    for v in op:
        if v == 'R':
            pb = not pb
        else:
            if pb:
                pre += 1
            else:
                back += 1
    if pre + back > n:
        print("error")
    else:
        res = list(map(str, nums[pre:n - back]))
        print("[" + ",".join(res if pb else res[::-1]) + "]")
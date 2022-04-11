def toNum(num):
    n = 0
    for v in num:
        n *= 10
        n += v
    return n

def backtrack(pre, dep):
    if dep == 10:
        return
    for v in range(pre):
        if v not in num:
            num.append(v)
            nums.append(toNum(num))
            backtrack(v, dep + 1)
            num.pop()

N = int(input())
nums = list(range(10))
num = []
for i in range(10):
    num.append(i)
    backtrack(i, 1)
    num.pop()
nums.sort()
print(nums[N] if N < len(nums) else -1)
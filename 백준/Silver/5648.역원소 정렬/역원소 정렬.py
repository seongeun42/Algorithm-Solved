import sys
input = sys.stdin.readline
n = input().split()
nums = []
for v in n[1:]:
    nums.append(int(''.join(v[::-1])))
n = int(n[0]) - len(nums)
while n:
    tmp = input().split()
    for v in tmp:
        nums.append(int(''.join(v[::-1])))
    n -= len(tmp)
print(*sorted(nums), sep='\n')
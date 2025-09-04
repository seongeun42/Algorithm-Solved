from collections import deque

N = int(input())
nums = deque(list(range(1, N + 1)))
turn = 1
while len(nums) > 1:
    left = (turn ** 3) % len(nums)
    if left != 1:
        nums.rotate(1 - left)
    nums.popleft()
    turn += 1
print(nums.popleft())
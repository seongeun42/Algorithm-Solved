from itertools import combinations as combi
nums = [int(input()) for _ in range(9)]
for c in combi(nums, 7):
    if sum(c) == 100:
        print(*c, sep='\n')
        break
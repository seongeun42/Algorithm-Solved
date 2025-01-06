from itertools import combinations
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    ans = 0
    max_v = 0
    for i in range(1, N + 1):
        nums = [*map(int, input().split())]
        for cb in combinations(nums, 3):
            one = sum(cb) % 10
            if max_v <= one:
                ans = i
                max_v = one
    print(ans)

solve()
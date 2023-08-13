import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)

def cycle(nums, chk, idx, c):
    if chk[idx] != 0:
        return 1 if chk[idx] == c else 0
    chk[idx] = c
    return cycle(nums, chk, nums[idx] - 1, c)

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        nums = [*map(int, input().split())]
        chk = [0] * N
        ans = 0
        for i in range(N):
            if chk[i] == 0:
                ans += cycle(nums, chk, i, i + 1)
        print(ans)

solve()
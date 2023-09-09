from itertools import permutations as pm
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    nums = [input().rstrip() for _ in range(n)]
    ans = set()
    for v in pm(nums, k):
        ans.add("".join(v))
    print(len(ans))
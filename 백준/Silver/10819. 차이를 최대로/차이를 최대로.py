from itertools import permutations as permu

def cal(arr):
    ans = 0
    for i in range(len(arr) - 1):
        ans += abs(arr[i] - arr[i + 1])
    return ans

N = int(input())
A = [*map(int, input().split())]
res = -1e9
for v in permu(A, N):
    res = max(res, cal(v))
print(res)
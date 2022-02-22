import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
ss = [int(input()) for _ in range(N)]
l = 0
res = 0
while l < N:
    r = (l + k) % N
    arr = set(ss[l:r]) if l < r else set(ss[l:] + ss[:r])
    cnt = len(arr) if c in arr else len(arr) + 1
    res = max(res, cnt)
    l += 1
print(res)
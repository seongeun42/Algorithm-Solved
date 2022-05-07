N = int(input())
M = int(input())
I = sorted([*map(int, input().split())])
l, r = 0, N - 1
cnt = 0
while l < r:
    hap = I[l] + I[r]
    if hap == M:
        cnt += 1
        l += 1
    elif hap < M:
        l += 1
    else:
        r -= 1
print(cnt)
import sys
input = sys.stdin.readline

N = int(input())
A = sorted([*map(int, input().split())])
ans = 0
for i in range(N - 2):
    l, r = i + 1, N - 1
    max_idx = N
    while l < r:
        hap = A[i] + A[l] + A[r]
        if hap < 0:
            l += 1
        elif hap == 0:
            if A[l] == A[r]:
                ans += r - l
            else:
                if max_idx > r:
                    max_idx = r
                    while max_idx >= 0 and A[max_idx - 1] == A[r]:
                        max_idx -= 1
                ans += r - max_idx + 1
            l += 1
        else:
            r -= 1
            
print(ans)
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    arr = sorted([*map(int, input().split())])
    maxV = 4000000000
    ans = []
    for i in range(N - 2):
        s, e = i + 1, N - 1
        while s < e:
            hap = arr[i] + arr[s] + arr[e]
            if abs(hap) < maxV:
                maxV = abs(hap)
                ans = [arr[i], arr[s], arr[e]]
            if hap < 0:
                s += 1
            elif hap > 0:
                e -= 1
            else:
                return ans
    return ans

print(*solve())
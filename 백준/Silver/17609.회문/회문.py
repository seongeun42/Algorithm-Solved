import sys
input = sys.stdin.readline

def palin(l, r, dif):
    if dif >= 2:
        return 2
    while l <= r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            a = palin(l, r - 1, dif + 1)
            b = palin(l + 1, r, dif + 1)
            return min(a, b)
    return dif

T = int(input())
for _ in range(T):
    s = input().strip()
    print(palin(0, len(s)-1, 0))
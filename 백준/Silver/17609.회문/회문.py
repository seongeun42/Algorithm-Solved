import sys
input = sys.stdin.readline

def check(L, R):
    while L <= R:
        if s[L] == s[R]:
            L += 1
            R -= 1
        else:
            return 0
    return 1

T = int(input())
for _ in range(T):
    s = input().strip()
    l, r = 0, len(s) - 1
    while l <= r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            if r > 0 and s[l] == s[r - 1]:
                if check(l, r - 1):
                    print(1)
                    break
            if l < len(s) - 1 and s[l + 1] == s[r]:
                if check(l + 1, r):
                    print(1)
                    break
            print(2)
            break
    if l > r:
        print(0)
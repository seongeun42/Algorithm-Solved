import sys
input = sys.stdin.readline

def solve():
    num = {"/": -1, "-": 0, "\\": 1, "(": 2, "@": 3,
           "?": 4, ">": 5, "&": 6, "%": 7}
    while 1:
        s = input().rstrip()
        if s == "#":
            return
        ans = 0
        for i in range(len(s)):
            ans += num[s[i]] * (8 ** (len(s) - i - 1))
        print(ans)

solve()
import sys
input = sys.stdin.readline

mo = set(list("aeiou"))
ja = set(list("bcdfghjklmnpqrstvwxyz"))

def check(s):
    if len(mo & set(list(s))) == 0:
        return False
    cnt = 1
    cur = 0 if s[0] in mo else 1
    for i in range(1, len(s)):
        if s[i] not in ["e", "o"] and s[i - 1] == s[i]:
            return False
        if cur == 0:
            if s[i] in mo:
                cnt += 1
            else:
                cnt, cur = 1, 1
        elif cur == 1:
            if s[i] in ja:
                cnt += 1
            else:
                cnt, cur = 1, 0
        if cnt == 3:
            return False
    return True

while 1:
    s = input().rstrip()
    if s == "end":
        break
    if check(s):
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")
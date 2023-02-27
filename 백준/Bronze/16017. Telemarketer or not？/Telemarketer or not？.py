s = [int(input()) for _ in range(4)]
if s[0] in [8, 9] and s[3] in [8, 9] and s[1] == s[2]:
    print("ignore")
else:
    print("answer")
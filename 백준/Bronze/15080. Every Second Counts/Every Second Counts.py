s = [*map(int, input().split(" : "))]
e = [*map(int, input().split(" : "))]
sn = s[0] * 60 * 60 + s[1] * 60 + s[2]
en = e[0] * 60 * 60 + e[1] * 60 + e[2]
if sn > en:
    en += 24 * 60 * 60
print(en - sn)
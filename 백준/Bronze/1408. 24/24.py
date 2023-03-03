cH, cM, cS = map(int, input().split(":"))
sH, sM, sS = map(int, input().split(":"))
c = cH * 60 * 60 + cM * 60 + cS
s = sH * 60 * 60 + sM * 60 + sS
a = s - c
if a < 0:
    a += 24 * 60 * 60
aH, aM, aS = a // 3600, (a % 3600) // 60, a % 60
print("%02d:%02d:%02d" % (aH, aM, aS))
n = int(input())
room = [input() for _ in range(n)]
rcnt, ccnt = 0, 0
for i in range(n):
    cs = "".join([room[j][i] for j in range(n)]).split("X")
    rs = room[i].split("X")
    for j in range(len(rs)):
        if len(rs[j]) >= 2:
            rcnt += 1
    for j in range(len(cs)):
        if len(cs[j]) >= 2:
            ccnt += 1
print(rcnt, ccnt)
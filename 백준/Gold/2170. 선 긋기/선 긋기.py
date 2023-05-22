import sys
input = sys.stdin.readline

n = int(input())
xyd = []
for _ in range(n):
    x, y = map(int, input().split())
    xyd.append((y - x, x, y))
xyd.sort(key=lambda x: (-x[0], x[1], x[2]))
line = []
ans = 0
for d, x, y in xyd:
    flag = 0
    ss, ee = [1e10, -1], [-1e10, -1]
    for i in range(len(line)):
        s, e = line[i]
        if y <= s or x >= e:
            continue
        if x < s and s < ss[0]:
            ss = [s, i]
        if y > e and e > ee[0]:
            ee = [e, i]
        flag = 1
    if flag == 0:
        ans += y - x
        line.append((x, y))
    else:
        if ss[0] != 1e10 and x < ss[0]:
            ans += (ss[0] - x)
            line[ss[1]] = [x, line[ss[1]][1]]
        if ee[0] != -1e10 and y > ee[0]:
            ans += (y - ee[0])
            line[ee[1]] = [line[ee[1]][0], y]
print(ans)
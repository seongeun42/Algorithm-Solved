def solution(routes):
    chk = set()
    carIn = sorted([[routes[i][0], i] for i in range(len(routes))])
    carOut = sorted([[routes[i][1], i] for i in range(len(routes))])
    ans = 0
    for i in range(len(routes)):
        ok = 0
        if carOut[i][1] in chk:
            continue
        for j in range(len(routes)):
            if carIn[j][0] <= carOut[i][0]:
                if carIn[j][1] not in chk:
                    chk.add(carIn[j][1])
                    ok = 1
            else:
                break
        if ok:
            ans += 1
    return ans
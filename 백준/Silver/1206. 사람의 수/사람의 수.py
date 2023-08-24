import math
N = int(input())
score = [input() for _ in range(N)]
res = 1
while res:
    flag = 0
    for v in score:
        s = str(math.ceil(int(v.replace(".", "")) * res / 1000) / res)
        i, cnt, dot = 0, 0, 0
        k = ""
        while i < len(s) and cnt < 3:
            if s[i] == ".":
                k += "."
                dot = 1
            else:
                k += s[i]
                if dot == 1:
                    cnt += 1
            i += 1
        while cnt < 3:
            k += "0"
            cnt += 1
        if k != v:
            flag = 1
            break
    if not flag:
        print(res)
        break
    res += 1
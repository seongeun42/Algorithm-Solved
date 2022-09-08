def solution(dartResult):
    i, cnt = 0, -1
    num = [0, 0, 0]
    score = {'S': 1, 'D': 2, 'T': 3}
    
    while i < len(dartResult):
        c = dartResult[i]
        if c.isdigit():
            cnt += 1
            num[cnt] = int(c)
            if dartResult[i + 1] == '0':
                num[cnt] = 10
                i += 1
        elif c == '*':
            if cnt > 0:
                num[cnt - 1] *= 2
            num[cnt] *= 2
        elif c == '#':
            num[cnt] *= -1
        else:
            num[cnt] = num[cnt] ** score[c]
        i += 1
            
    return sum(num)
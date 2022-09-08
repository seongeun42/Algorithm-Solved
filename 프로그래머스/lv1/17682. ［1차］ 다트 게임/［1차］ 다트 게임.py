def solution(dartResult):
    i, cnt = 0, -1
    dartResult = dartResult.replace("10", "a")
    num = [0, 0, 0]
    score = {'S': 1, 'D': 2, 'T': 3}
    
    while i < len(dartResult):
        c = dartResult[i]
        if c.isdigit() or c == 'a':
            cnt += 1
            num[cnt] = int(c) if c != 'a' else 10
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
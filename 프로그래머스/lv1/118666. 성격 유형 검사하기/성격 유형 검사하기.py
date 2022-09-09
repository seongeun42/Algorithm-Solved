def solution(survey, choices):
    answer = ''
    score = [0, 3, 2, 1, 0, 1, 2, 3]
    type = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    # 점수 계산
    for i in range(len(survey)):
        c = survey[i][0] if choices[i] < 4 else survey[i][1]
        type[c] += score[choices[i]]
        
    # 유형 판별
    for t in ["RT", "CF", "JM", "AN"]:
        answer += t[0] if type[t[0]] >= type[t[1]] else t[1]
        
    return answer
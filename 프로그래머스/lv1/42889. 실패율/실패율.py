def solution(N, stages):
    answer = []
    stagePeopleCnt = [0] * (N + 2)
    
    for i in range(len(stages)):
        stagePeopleCnt[stages[i]] += 1
        
    people = stagePeopleCnt[N + 1]
    for i in range(N, 0, -1):
        people += stagePeopleCnt[i]
        failRate = stagePeopleCnt[i] / people if people != 0 else 0
        answer.append([i, failRate])
        
    answer = sorted(answer, key=lambda x : (-x[1], x[0]))
    
    return [arr[0] for arr in answer]
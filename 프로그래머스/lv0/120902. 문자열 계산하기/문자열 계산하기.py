def solution(my_string):
    epr = my_string.split()
    answer = int(epr[0])
    for i in range(2, len(epr), 2):
        op = 1 if epr[i - 1] == "+" else -1 
        answer += op * int(epr[i])
    return answer
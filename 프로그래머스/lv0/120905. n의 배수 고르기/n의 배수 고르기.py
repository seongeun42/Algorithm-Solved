def solution(n, numlist):
    answer = []
    for c in numlist:
        if c % n == 0:
            answer.append(c)
    return answer
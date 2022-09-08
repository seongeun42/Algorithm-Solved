def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        line = bin(arr1[i] | arr2[i])[2:].rjust(n, "0")
        line = line.replace('0', ' ')
        line = line.replace('1', '#')
        answer.append(line)
    return answer
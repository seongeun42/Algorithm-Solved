def solution(n):
    for i in range(2, 1000000):
        if n % i == 1:
            return i
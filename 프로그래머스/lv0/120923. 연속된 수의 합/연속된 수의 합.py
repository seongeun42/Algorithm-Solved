def solution(num, total):
    start = (total * 2 // num - num + 1) // 2
    return list(range(start, start + num))
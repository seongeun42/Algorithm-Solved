def solution(num, total):
    if total == 0:
        end = (num - 1) // 2
        return list(range(-end, end + 1))
    end = total + 1
    while 1:
        if sum(range(end - num, end)) == total:
            return list(range(end - num, end))
        end -= 1
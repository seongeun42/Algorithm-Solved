def solution(num, k):
    ans = str(num).find(str(k)) + 1
    return ans if ans != 0 else -1
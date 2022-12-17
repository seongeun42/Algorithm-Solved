def solution(common):
    cha = common[1] - common[0]
    if common[-1] - common[0] == cha * (len(common) - 1):
        return common[-1] + cha
    return common[-1] * (common[1] // common[0])
def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for w in words:
            b = b.replace(w, ".")
        if len(b.replace(".", "")) == 0:
            answer += 1
    return answer
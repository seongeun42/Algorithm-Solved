def check(word):
    p = {"a": "aya", "y": "ye", "w": "woo", "m": "ma"}
    i = 0
    while i < len(word):
        if word[i] not in p or word[i:i + len(p[word[i]])] != p[word[i]]:
            return 0
        i += len(p[word[i]]) if word[i] in p else 1
    return 1

def solution(babbling):
    answer = 0
    for w in babbling:
        answer += check(w)
    return answer
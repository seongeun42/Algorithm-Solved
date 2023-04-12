def solution(name):
    l = len(name)
    A = ord('A')
    cnt = [i for i in range(14)] + [i for i in range(12, 0, -1)]
    answer = sum([cnt[ord(c) - A] for c in name])
    move = l - 1
    for i in range(l):
        next_i = i + 1
        while next_i < l and name[next_i] == 'A':
            next_i += 1
        move = min(move, 2 * i + l - next_i, 2 * (l - next_i) + i)
    return answer + move
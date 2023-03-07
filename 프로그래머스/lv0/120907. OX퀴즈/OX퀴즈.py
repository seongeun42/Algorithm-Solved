def solution(quiz):
    answer = []
    op = {'-': -1, '+': 1}
    for me in quiz:
        me = me.split()
        ans = 'O' if int(me[0]) + op[me[1]] * int(me[2]) == int(me[4]) else 'X'
        answer.append(ans)
    return answer
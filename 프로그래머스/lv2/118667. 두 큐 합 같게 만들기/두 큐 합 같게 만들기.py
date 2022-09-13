from collections import deque
def solution(queue1, queue2):
    s1, s2 = sum(queue1), sum(queue2)
    if (s1 + s2) % 2:
        return -1
    answer = 0
    q1, q2 = deque(queue1), deque(queue2)
    while s1 != s2:
        if answer > 2 * (len(queue1) + len(queue2)):
            return -1
        if s1 > s2:
            s2 += q1[0]
            s1 -= q1[0]
            q2.append(q1.popleft())
        else:
            s1 += q2[0]
            s2 -= q2[0]
            q1.append(q2.popleft())
        answer += 1
    return answer
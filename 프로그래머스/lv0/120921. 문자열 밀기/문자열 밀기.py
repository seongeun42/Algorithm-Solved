def solution(A, B):
    if not A: return 0
    for i in range(len(A)):
        if A == B[i:len(B)] + B[:i]:
            return i
    return -1
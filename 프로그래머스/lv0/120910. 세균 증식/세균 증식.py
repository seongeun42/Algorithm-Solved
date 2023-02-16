def solution(n, t):
    ans = n
    for _ in range(t):
        ans *= 2
    return ans
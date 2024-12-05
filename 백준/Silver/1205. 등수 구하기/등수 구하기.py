def solve():
    N, TS, P = map(int, input().split())
    if N == 0:
        return 1
    scores = [*map(int, input().split())]
    if N == P and scores[-1] >= TS:
        return -1
    ans = N + 1
    for i in range(N):
        if scores[i] <= TS:
            ans =  i + 1
            break
    return ans

print(solve())
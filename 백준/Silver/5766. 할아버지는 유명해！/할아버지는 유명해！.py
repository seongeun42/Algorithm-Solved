import sys
input = sys.stdin.readline

while 1:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    score = {}
    for _ in range(N):
        rank = [*map(int, input().split())]
        for v in rank:
            score[v] = score.get(v, 0) + 1
    score = sorted(score.items(), key=lambda x: (-x[1], x[0]))
    for i in range(1, len(score)):
        if score[i][1] < score[1][1]:
            break
        print(score[i][0], end=" ")
    print()
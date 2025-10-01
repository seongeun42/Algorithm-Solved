import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    score, count, time = [[0] * k for _ in range(n)], [0] * n, [0] * n
    for q in range(m):
        i, j, s = map(int, input().split())
        count[i - 1] += 1
        time[i - 1] = q
        if score[i - 1][j - 1] < s:
            score[i - 1][j - 1] = s
    total = [(sum(arr), count[i], time[i], i + 1)  for i, arr in enumerate(score)]
    total.sort(key=lambda x: (-x[0], x[1], x[2]))
    for i in range(n):
        if total[i][-1] == t:
            print(i + 1)
            break
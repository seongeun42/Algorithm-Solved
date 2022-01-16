import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  cnt = n
  score = [list(map(int, input().split())) for _ in range(n)]
  score.sort(key=lambda x: (x[0], x[1]))
  for i in range(1, n):
    if score[i][1] > score[i - 1][1]:
      cnt -= 1
      score[i][1] = score[i - 1][1]
  print(cnt)
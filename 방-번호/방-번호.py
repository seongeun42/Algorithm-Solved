n = map(int, list(input()))
dic = {k:0 for k in range(0, 10)}
cnt = 1
for v in n:
  dic[v] += 1
  if v != 9 and v != 6 and cnt < dic[v]:
    cnt = dic[v]
  elif v == 9 or v == 6:
    c = dic[9] + dic[6] - 1
    if cnt < c // 2 + 1: cnt = c // 2 + 1
print(cnt)
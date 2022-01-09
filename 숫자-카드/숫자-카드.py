n = int(input())
sg = {v:0 for v in list(map(int, input().split()))}
m = int(input())
mm = list(map(int, input().split()))
chk = [0] * m

for i in range(m):
  if mm[i] in sg:
    chk[i] = 1

print(*chk, sep=" ")
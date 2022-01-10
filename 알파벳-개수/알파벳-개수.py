s = input()
alph = {k:0 for k in list("abcdefghijklmnopqrstuvwxyz")}
for v in s:
  alph[v] += 1
print(*list(alph.values()), sep=" ")
a, b = [0] * 26, [0] * 26
s1 = list(input())
s2 = list(input())
cnt = 0
for v in s1:
  a[ord(v) - 97] += 1
for v in s2:
  b[ord(v) - 97] += 1
for i in range(26):
  cnt += abs(a[i] - b[i])
print(cnt)
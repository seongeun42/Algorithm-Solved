a = ord('a')
al = [0 for i in range(26)]
n = int(input())
flag = True
for _ in range(n):
    al[ord(input()[0]) - a] += 1
for i in range(26):
    if al[i] >= 5:
        print(chr(a + i), end="")
        flag = False
if flag:
    print("PREDAJA")
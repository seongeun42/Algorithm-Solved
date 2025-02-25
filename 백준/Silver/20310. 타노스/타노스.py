S = input()
zero = S.count('0') // 2
one = (len(S) - (zero * 2)) // 2
chk = [True] * len(S)
# 왼쪽에서부터 1 제거
for i in range(len(S)):
    if one == 0:
        break
    if S[i] == '1':
        chk[i] = False
        one -= 1
# 오른쪽에서부터 0 제거
for i in range(len(S) - 1, -1, -1):
    if zero == 0:
        break
    if S[i] == '0':
        chk[i] = False
        zero -= 1
print(''.join([S[i] for i in range(len(S)) if chk[i]]))
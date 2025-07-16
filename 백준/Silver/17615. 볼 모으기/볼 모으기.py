N = int(input())
RB = input()
R, B = 0, 0
first = [RB[0], 0]
last = [RB[-1], 0]
# 처음 문자
for i in range(N):
    if RB[i] == first[0]:
        first[1] += 1
    else:
        break
# 마지막 문자
for i in range(N - 1, -1, -1):
    if RB[i] == last[0]:
        last[1] += 1
    else:
        break
# 중간 문자
for i in range(first[1], N - last[1]):
    if RB[i] == 'R':
        R += 1
    else:
        B += 1
# R을 맨뒤로 미는 경우
rl = R + first[1] if first[0] == 'R' else R
# B를 맨뒤로 미는 경우
bl = B + first[1] if first[0] == 'B' else B
# R을 맨앞으로 미는 경우
rf = R + last[1] if last[0] == 'R' else R
# B를 맨앞으로 미는 경우
bf = B + last[1] if last[0] == 'B' else B
print(min(rl, bl, rf, bf))
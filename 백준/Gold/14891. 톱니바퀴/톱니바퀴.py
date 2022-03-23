def rotate(start, r):
    st = start
    if r == -1:
        st = 0 if st == 7 else st + 1
    else:
        st = 7 if st == 0 else st - 1
    return st

def state(s):
    stat = [0] * 3
    # 톱니바퀴1과 2의 맞닿는 부분 표시
    stat[0] = 0 if t[1][(s[1] + 2) % 8] == t[2][(s[2] + 6) % 8] else 1
    # 톱니바퀴2과 3의 맞닿는 부분 표시
    stat[1] = 0 if t[2][(s[2] + 2) % 8] == t[3][(s[3] + 6) % 8] else 1
    # 톱니바퀴3과 4의 맞닿는 부분 표시
    stat[2] = 0 if t[3][(s[3] + 2) % 8] == t[4][(s[4] + 6) % 8] else 1
    return stat

t = [0] + [input() for _ in range(4)]
s = [0] * 5
for _ in range(int(input())):
    n, r = map(int, input().split())
    stat = state(s)
    s[n] = rotate(s[n], r)
    # 오른쪽 톱니바퀴 회전 확인
    turn = r
    for i in range(n + 1, 5):
        turn *= -1
        if not stat[i - 2]:
            break
        else:
            s[i] = rotate(s[i], turn)
    # 왼쪽 톱니바퀴 회전 확인
    turn = r
    for i in range(n - 1, -1, -1):
        turn *= -1
        if not stat[i - 1]:
            break
        else:
            s[i] = rotate(s[i], turn)
res = 0
for i in range(1, 5):
    res += int(t[i][s[i]]) * (2 ** (i - 1))
print(res)
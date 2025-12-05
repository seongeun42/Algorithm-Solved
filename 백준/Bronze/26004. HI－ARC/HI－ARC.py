N = int(input())
S = input()
cnt = [0] * 5
for c in S:
    if c == 'H':
        cnt[0] += 1
    elif c == 'I':
        cnt[1] += 1
    elif c == 'A':
        cnt[2] += 1
    elif c == 'R':
        cnt[3] += 1
    elif c == 'C':
        cnt[4] += 1
print(min(cnt))
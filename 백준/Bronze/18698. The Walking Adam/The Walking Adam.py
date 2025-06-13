T = int(input())
for _ in range(T):
    S = input()
    cnt = 0
    for c in S:
        if c == 'D':
            break
        cnt += 1
    print(cnt)
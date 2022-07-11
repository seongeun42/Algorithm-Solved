N = int(input())
for _ in range(N):
    s = list(input())
    s[0] = s[0].upper()
    print(''.join(s))
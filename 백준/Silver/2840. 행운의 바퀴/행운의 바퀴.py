import sys
input = sys.stdin.readline

N, K = map(int, input().split())
wheel = ['?'] * N
cur = 0
used = set()
for _ in range(K):
    cnt, c = input().rstrip().split()
    cur = (cur - int(cnt)) % N
    if (wheel[cur] != '?' and wheel[cur] != c) or (wheel[cur] == '?' and c in used):
        print("!")
        exit()
    else:
        wheel[cur] = c
        used.add(c)
print(''.join(wheel[cur:]+wheel[:cur]))
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
train = [0b0] * N
for _ in range(M):
    cmd = [*map(int, input().split())]
    if cmd[0] == 1:
        train[cmd[1] - 1] |= 0b1 << (cmd[2] - 1)
    elif cmd[0] == 2:
        train[cmd[1] - 1] &= ~(0b1 << (cmd[2] - 1))
    elif cmd[0] == 3:
        train[cmd[1] - 1] <<= 1
        train[cmd[1] - 1] &= ~(0b1 << 20)
    else:
        train[cmd[1] - 1] >>= 1
print(len(set(train)))
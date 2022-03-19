K, S, N = input().split()
K = [ord(K[0]) - 65, 8 - int(K[1])]
S = [ord(S[0]) - 65, 8 - int(S[1])]
move = [input() for _ in range(int(N))]
cmd = {
    "R": [1, 0], "L": [-1, 0],
    "B": [0, 1], "T": [0, -1],
    "RT": [1, -1], "LT": [-1, -1],
    "RB": [1, 1], "LB": [-1, 1]
}
for m in move:
    if not (0 <= K[0] + cmd[m][0] < 8 and 0 <= K[1] + cmd[m][1] < 8):
        continue
    if K[0] + cmd[m][0] == S[0] and K[1] + cmd[m][1] == S[1]:
        if 0 <= S[0] + cmd[m][0] < 8 and 0 <= S[1] + cmd[m][1] < 8:
            S = [S[0] + cmd[m][0], S[1] + cmd[m][1]]
        else:
            continue
    K = [K[0] + cmd[m][0], K[1] + cmd[m][1]]
print(chr(K[0] + 65), 8 - K[1], sep='')
print(chr(S[0] + 65), 8 - S[1], sep='')
import sys
input = sys.stdin.readline

def check():
    for i in range(R):
        for j in range(C):
            if M[i][j] == 'W':
                for dx, dy in d:
                    a, b = j + dx, i + dy
                    if 0 <= a < C and 0 <= b < R and M[b][a] == 'S':
                        return 0
    return 1

R, C = map(int, input().split())
M = [input().strip().replace('.', 'D') for _ in range(R)]
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
flag = check()
print(flag)
if flag:
    print(*M, sep='\n')
N, M = map(int, input().split())
s = [list(input()) for _ in range(N)]
rotate = {'.': '.', 'O': 'O', '-': '|', '|': '-', '/': '\\', '\\': '/',
          '^': '<', '<': 'v', 'v': '>', '>': '^'}
ans = [[] for _ in range(M)]
for i in range(N):
    for j in range(M):
        ans[M - j - 1].append(rotate[s[i][j]])
for i in range(M):
    print(*ans[i], sep="")
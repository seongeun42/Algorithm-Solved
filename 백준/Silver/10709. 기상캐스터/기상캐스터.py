H, W = map(int, input().split())
cloud = [list(input()) for _ in range(H)]
ans = [[-1] * W for _ in range(H)]
for i in range(H):
    c = -1
    for j in range(W):
        if c != -1:
            c += 1
        if cloud[i][j] == 'c':
            c = 0
        ans[i][j] = c

for i in range(H):
    print(*ans[i])
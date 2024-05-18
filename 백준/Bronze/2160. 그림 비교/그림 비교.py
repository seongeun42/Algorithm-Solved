N = int(input())
pics = [[input() for _ in range(5)] for _ in range(N)]
ans = [0, 0]
cnt = 36
for i in range(N):
    for j in range(i + 1, N):
        tmp = 0
        for r in range(5):
            for c in range(7):
                if pics[i][r][c] != pics[j][r][c]:
                    tmp += 1
        if cnt > tmp:
            cnt = tmp
            ans[0], ans[1] = i + 1, j + 1
print(*ans)
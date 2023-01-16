n = [[*map(int, input().split())] for i in range(9)]
ans = [0, 0]
for i in range(9):
    for j in range(9):
        if n[ans[0]][ans[1]] < n[i][j]:
            ans = [i, j]
print(n[ans[0]][ans[1]])
print(ans[0] + 1, ans[1] + 1)
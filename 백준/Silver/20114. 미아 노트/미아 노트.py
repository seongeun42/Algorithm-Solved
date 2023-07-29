N, H, W = map(int, input().split())
strs = [list(input()) for _ in range(H)]
ans = ""
for i in range(1, H):
    for j in range(N * W):
        if strs[0][j] != "?": continue
        if strs[i][j] != "?":
            strs[0][j] = strs[i][j]
for i in range(0, N * W, W):
    c = "?"
    for j in range(i, i + W):
        if strs[0][j] != "?":
            c = strs[0][j]
    ans += c
print(ans)
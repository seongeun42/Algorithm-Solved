N, H, W = map(int, input().split())
ans = ['?'] * N
for _ in range(H):
    s = input()
    for i in range(N * W):
        if s[i] != '?':
            ans[i // W] = s[i]
print("".join(ans))
N, L = input().split()
N = int(N)
ans, cnt = 0, 0
while cnt < N:
    ans += 1
    if L not in str(ans):
        cnt += 1
print(ans)
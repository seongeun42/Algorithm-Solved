N = int(input())
tanghuru = [*map(int, input().split())]
cnt = [0] * 10
cnt[tanghuru[0]] += 1
l, r = 0, 0
fruits, ans = 1, 1
while r < N - 1 or fruits > 2:
    if fruits <= 2 and r < N - 1:
        r += 1
        if cnt[tanghuru[r]] == 0:
            fruits += 1
        cnt[tanghuru[r]] += 1
    if fruits > 2:
        cnt[tanghuru[l]] -= 1
        if cnt[tanghuru[l]] == 0:
            fruits -= 1
        l += 1
    if r - l + 1 > ans:
        ans = r - l + 1
print(ans)
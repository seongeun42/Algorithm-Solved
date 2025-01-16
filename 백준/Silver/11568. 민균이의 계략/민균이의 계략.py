N = int(input())
card = [*map(int, input().split())]
cnt = [0] * N
for i in range(N):
    for j in range(i):
        if card[i] > card[j] and cnt[i] < cnt[j]:
            cnt[i] = cnt[j]
    cnt[i] += 1
print(max(cnt))
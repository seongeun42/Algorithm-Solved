N, X = map(int, input().split())
cnt = [*map(int, input().split())]
arr = [sum(cnt[:X])]
for i in range(X, N):
    arr.append(arr[-1] + cnt[i] - cnt[i - X])
ans = max(arr)
if ans == 0:
    print("SAD")
else:
    print(ans, arr.count(ans), sep="\n")
N, K = map(int, input().split())
W = sorted([*map(int, input().split())])
l, r = 0, N - 1
ans = 0
while l < r:
    cats = W[l] + W[r] 
    if cats <= K:
        ans += 1
        l += 1
        r -= 1
    elif cats > K:
        r -= 1
print(ans)
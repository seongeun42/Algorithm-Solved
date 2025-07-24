N = int(input())
size = sorted([*map(int, input().split())])
ans = 0
for i in range(N):
    s, e = i + 1, N - 1
    idx = -1
    while s <= e:
        mid = (s + e) // 2
        if size[i] * 10 >= size[mid] * 9:
            s = mid + 1
            idx = mid
        else:
            e = mid - 1
    ans += idx - i if idx != -1 else 0

print(ans)
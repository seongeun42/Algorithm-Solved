N = int(input())
drink = sorted([*map(int, input().split())])
ans = drink.pop()
for i in range(N - 1):
    ans += drink[i] / 2
print(int(ans) if ans % 1  == 0 else ans)
N = int(input())
drink = sorted([*map(int, input().split())])
ans = drink.pop() + (sum(drink) / 2)
print(int(ans) if ans % 1  == 0 else ans)
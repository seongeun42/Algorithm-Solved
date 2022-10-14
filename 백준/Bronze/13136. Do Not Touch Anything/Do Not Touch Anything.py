r, c, n = map(int, input().split())
ans = r // n if r % n == 0 else r // n + 1
ans *= c // n if c % n == 0 else c // n + 1
print(ans)
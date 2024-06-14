N = int(input())
money = {
    "136 68": 1000,
    "142 68": 5000,
    "148 68": 10000,
    "154 68": 50000
    }
ans = 0
for _ in range(N):
    ans += money[input()]
print(ans)
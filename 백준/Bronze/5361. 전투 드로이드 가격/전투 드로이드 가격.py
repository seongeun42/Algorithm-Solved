price = [350.34, 230.9, 190.55, 125.3, 180.9]
t = int(input())
for _ in range(t):
    cnt = [*map(int, input().split())]
    ans = sum([cnt[i] * price[i] for i in range(5)])
    print(f"${ans:.2f}")
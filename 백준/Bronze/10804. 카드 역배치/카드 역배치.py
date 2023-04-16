card = [i for i in range(1, 21)]
for _ in range(10):
    s, e = map(int, input().split())
    card[s-1:e] = card[s-1:e][::-1]
print(*card)
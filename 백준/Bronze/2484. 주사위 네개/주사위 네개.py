import sys
input = sys.stdin.readline

N = int(input())
ans = 0
for _ in range(N):
    dice = [*map(int, input().split())]
    cnt = [0] * 7
    for d in dice:
        cnt[d] += 1
    money = [0] * 4
    for i in range(1, 7):
        if cnt[i] == 4:
            money[3] = 50000 + i * 5000
        elif cnt[i] == 3:
            money[2] = 10000 + i * 1000
        elif cnt[i] == 2 and money[1] == 0:
            money[1] = 1000 + i * 100
        elif cnt[i] == 2 and money[1] > 0:
            pre = (money[1] - 1000) // 100
            money[1] = 2000 + i * 500 + pre * 500
        elif cnt[i] == 1 and i > money[0] // 100:
            money[0] = i * 100
    ans = max(ans, max(money))
print(ans)
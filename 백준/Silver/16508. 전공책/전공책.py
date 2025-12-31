import sys
input = sys.stdin.readline

T = input().rstrip()
target = {}
for c in T:
    target[c] = target.get(c, 0) + 1
N = int(input())
book = []
for _ in range(N):
    price, title = input().rstrip().split()
    book.append((title, int(price)))
ans = 2_000_000
for i in range(1 << N):
    pick = []
    for j in range(N):
        if i & (1 << j):
            pick.append(book[j])
    total_price = 0
    alpha = {}
    cnt = 0
    for title, price in pick:
        have = False
        for c in title:
            if c in target and alpha.get(c, 0) < target[c]:
                alpha[c] = alpha.get(c, 0) + 1
                cnt += 1
                have = True
        if have:
            total_price += price
    if cnt == len(T) and total_price < ans:
        ans = total_price
print(ans if ans != 2_000_000 else -1)
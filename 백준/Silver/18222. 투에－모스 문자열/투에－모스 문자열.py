def solve():
    k = int(input())
    cnt = 0
    i = 1
    while i * 2 < k:
        i *= 2
    while k != 1:
        if i < k:
            cnt +=1
            k -= i
        i //= 2
    print(1 if cnt % 2 else 0)

solve()
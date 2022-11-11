def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

t = int(input())
for _ in range(t):
    n = [*map(int, input().split())]
    ans = 0
    for i in range(1, n[0]):
        for j in range(i + 1, n[0] + 1):
            ans += gcd(n[i], n[j])
    print(ans)
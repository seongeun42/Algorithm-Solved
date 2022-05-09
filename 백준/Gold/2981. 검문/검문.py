import sys
input = sys.stdin.readline

def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

N = int(input())
su = sorted([int(input()) for _ in range(N)], reverse=True)
gcd_num = gcd(su[0] - su[1], su[1] - su[2]) if N > 2 else su[0] - su[1]
for i in range(2, N - 1):
    gcd_num = gcd(gcd_num, su[i] - su[i + 1])
divisor = {gcd_num}
for i in range(2, gcd_num + 1):
    if i * i > gcd_num:
        break
    if gcd_num % i == 0:
        divisor.add(i)
        divisor.add(gcd_num // i)
print(*sorted(list(divisor)))
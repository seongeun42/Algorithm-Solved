import sys
input = sys.stdin.readline

ans = int(input())
while 1:
    v = input().rstrip()
    if v == '=':
        break
    if v == '+':
        ans += int(input())
    elif v == '-':
        ans -= int(input())
    elif v == '*':
        ans *= int(input())
    elif v == '/':
        ans //= int(input())
print(ans)
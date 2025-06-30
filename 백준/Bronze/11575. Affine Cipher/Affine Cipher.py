import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    s = input().rstrip()
    res = ''.join([chr(ord('A') + ((ord(c)-ord('A'))*a + b)%26) for c in s])
    print(res)
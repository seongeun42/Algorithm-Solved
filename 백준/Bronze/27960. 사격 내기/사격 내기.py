import sys
input = sys.stdin.readline

a, b = map(int, input().split())
bin_a = bin(a)
bin_b = bin(b)
print(int(bin(a^b)[2:], 2))
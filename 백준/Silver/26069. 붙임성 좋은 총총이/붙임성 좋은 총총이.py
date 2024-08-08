import sys
input = sys.stdin.readline

N = int(input())
dancing = {"ChongChong"}
for _ in range(N):
    a, b = input().split()
    if a in dancing:
        dancing.add(b)
    elif b in dancing:
        dancing.add(a)
print(len(dancing))
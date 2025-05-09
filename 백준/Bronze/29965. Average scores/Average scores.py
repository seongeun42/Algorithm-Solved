import sys
input = sys.stdin.readline

N = int(input())
M, J = [0, 0], [0, 0]
for _ in range(N):
    p, s = input().rstrip().split()
    if p == 'M':
        M[0] += 1
        M[1] += int(s)
    else:
        J[0] += 1
        J[1] += int(s)
m = M[1] / M[0] if M[0] > 0 else 0
j = J[1] / J[0] if J[0] > 0 else 0
if m < j:
    print("J")
elif m > j:
    print("M")
else:
    print("V")
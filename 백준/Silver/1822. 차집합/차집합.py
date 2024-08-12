import sys
input = sys.stdin.readline

_ = input()
A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = A - B
print(len(C))
if C:
    print(*sorted(list(C)))
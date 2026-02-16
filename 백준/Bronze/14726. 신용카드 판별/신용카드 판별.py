import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num = input().rstrip()
    total = 0
    for i in range(15, -1, -1):
        if i % 2 == 0:
            total += sum(map(int, str(int(num[i]) * 2)))
        else:
            total += int(num[i])
    print("T" if total % 10 == 0 else "F")
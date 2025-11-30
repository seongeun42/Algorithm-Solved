import sys
input = sys.stdin.readline

N = int(input())
arr = [v % 2 for v in [*map(int, input().split())]]
odd, even = 0, 0
desc, asc = 0, 0
for v in arr:
    if v == 1:
        odd += 1
        desc += even
    else:
        even += 1
        asc += odd
print(min(desc, asc))
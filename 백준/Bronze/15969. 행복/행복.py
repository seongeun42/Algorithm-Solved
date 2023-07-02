n = int(input())
s = sorted([*map(int, input().split())])
print(s[-1] - s[0])
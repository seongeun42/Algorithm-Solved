n = int(input())
H = [*map(int, input().split())]
A = [*map(int, input().split())]
HA = sorted([*map(list, zip(A, H))])
print(sum([HA[i][1] + HA[i][0] * i for i in range(n)]))
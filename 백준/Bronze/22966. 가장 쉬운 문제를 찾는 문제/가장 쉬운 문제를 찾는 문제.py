N = int(input())
sub = sorted([input().split() for _ in range(N)], key=lambda x: x[1])
print(sub[0][0])
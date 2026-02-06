N = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
print(sum([b[i] - a[i] for i in range(N) if b[i] - a[i] > 0]))
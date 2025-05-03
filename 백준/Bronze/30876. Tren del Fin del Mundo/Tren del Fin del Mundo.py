N = int(input())
arr = sorted([[*map(int, input().split())] for _ in range(N)], key=lambda x: x[1])
print(*arr[0])
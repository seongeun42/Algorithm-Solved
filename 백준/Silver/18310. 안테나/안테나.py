N = int(input())
H = sorted([*map(int, input().split())])
print(H[N // 2] if N % 2 else H[N // 2 - 1])
N = int(input())
T = [*map(int, input().split())]
print(*divmod((len(T) - 1) * 8 + sum(T), 24))